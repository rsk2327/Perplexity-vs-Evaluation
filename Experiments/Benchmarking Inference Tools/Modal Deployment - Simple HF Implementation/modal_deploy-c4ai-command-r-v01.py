# Based on https://modal.com/docs/examples/vllm_mixtral

import os
import time

import modal

MODEL_DIR = "/model"
MODEL_NAME = "CohereForAI/c4ai-command-r-v01"
MODEL_REVISION = "16881ccde1c68bbc7041280e6a66637bc46bfe88"
GPU_CONFIG = modal.gpu.A100(size="80GB", count=2)

def download_model_to_image(model_dir, model_name, model_revision):
    from huggingface_hub import snapshot_download
    from transformers.utils import move_cache

    os.makedirs(model_dir, exist_ok=True)

    snapshot_download(
        model_name,
        revision=model_revision,
        local_dir=model_dir,
        ignore_patterns=["*.pt", "*.bin"],  # Using safetensors
    )
    move_cache()

hf_image = (
    modal.Image.debian_slim(python_version="3.10")
    .pip_install(
        "torch==2.1.2",
        "transformers==4.39.3",
        "hf-transfer==0.1.6",
        "huggingface_hub==0.22.2",
        "accelerate"
    )
    .env({
        "HF_HUB_ENABLE_HF_TRANSFER": "1",
        "HF_TOKEN": "" # Add your Hugging Face token here. The secret route in Modal doesn't seem to work
        })
    .run_function(
        download_model_to_image,
        timeout=60 * 20,
        kwargs={
            "model_dir": MODEL_DIR,
            "model_name": MODEL_NAME,
            "model_revision": MODEL_REVISION,
        },
    )
)

app = modal.App("c4ai-command-r-v01-batch-perplexity-inference")

@app.cls(
    gpu=GPU_CONFIG,
    timeout=60 * 10,
    container_idle_timeout=60 * 10,
    allow_concurrent_inputs=10,
    image=hf_image,
    secrets=[modal.Secret.from_name("my-huggingface-secret")]
)
class Model:
    @modal.enter()
    def start_engine(self):

        print("🥶 cold starting inference")
        start = time.monotonic_ns()

        from transformers import AutoTokenizer, AutoModelForCausalLM

        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_auth_token = os.environ["HF_TOKEN"], trust_remote_code=True, device_map="auto")
        self.model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, use_auth_token = os.environ["HF_TOKEN"], trust_remote_code=True, device_map="auto")

        self.device = "cuda"

        duration_s = (time.monotonic_ns() - start) / 1e9
        print(f"Model loaded in {duration_s:.0f}s")

    @modal.method()
    async def get_perplexity_for_batch(self, batch_of_strings):
        # Reference: https://huggingface.co/docs/transformers/en/perplexity

        import torch
        from tqdm import tqdm

        encodings = self.tokenizer(batch_of_strings, return_tensors="pt", padding=True, truncation=True)

        encodings = {k: v.to(self.device) for k, v in encodings.items()}

        with torch.no_grad():
            outputs = self.model(**encodings, labels=encodings["input_ids"])

        loss = outputs.loss.item()
        ppl = torch.exp(torch.tensor(loss)).item()

        return ppl
        

    # @modal.exit()
    # def stop_engine(self):
    #     if GPU_CONFIG.count > 1:
    #         import ray

    #         ray.shutdown()

