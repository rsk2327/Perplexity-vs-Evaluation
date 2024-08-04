# Benchmarking Different Inference Libraries for Obtaining Perplexities

- vLLM: Not suitable because it does return logits for the prompt. See: https://github.com/vllm-project/vllm/issues/2364
- SGLang: Again same issue as vLLM, they do not store KV cache for shared prefixes and presumably that extends to entire prompt. See: https://github.com/sgl-project/sglang/issues/81#issuecomment-1905793473
- Native HF: Works, examples in `Modal Deployment - Simple HF Implementation/`
- TensorRT: Seems to support logits for prompt but does not support Command Models (https://github.com/NVIDIA/TensorRT-LLM/issues/1360, https://github.com/NVIDIA/TensorRT-LLM/issues/1657)

# Runtimes - 

Average of 10 runs with same sample


| **Model**             | **Inference Method** | **GPU**           |                 **Average Time/Sample** |
|-----------------------|----------------------|-------------------|----------------------------------------:|
| CohereForAI/aya-23-8B | Huggingface          | A100-80GB (Modal) | 1.39 Seconds (Excluding Coldstart Time) |
| CohereForAI/aya-23-35B | Huggingface          | 2xA100-80GB (Modal) | 2.04 Seconds (Excluding Coldstart Time) |
| CohereForAI/c4ai-command-r-plus-4bit | Huggingface          | ToDo | ToDo |
| CohereForAI/c4ai-command-r-plus | Huggingface          | 2xA100-80GB (Modal) | 1.99 Seconds (Excluding Coldstart Time) |
| CohereForAI/c4ai-command-r-v01-4bit | Huggingface          | ToDo | ToDo |
| CohereForAI/c4ai-command-r-v01 (Note: Got very high perplexities with same setup, need to debug) | Huggingface          | 3xA100-80GB (Modal) | 44.87 Seconds (Excluding Coldstart Time) |

