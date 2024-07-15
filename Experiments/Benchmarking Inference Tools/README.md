# Benchmarking Different Inference Libraries for Obtaining Perplexities

- vLLM: Not suitable because it does return logits for the prompt. See: https://github.com/vllm-project/vllm/issues/2364
- SGLang: Again same issue as vLLM, they do not store KV cache for shared prefixes and presumably that extends to entire prompt. See: https://github.com/sgl-project/sglang/issues/81#issuecomment-1905793473
- Native HF: Works, example in `modal_deploy.py`

# Runtimes - 

Average of 10 runs with same sample


| **Model**             | **Inference Method** | **GPU**           |                 **Average Time/Sample** |
|-----------------------|----------------------|-------------------|----------------------------------------:|
| CohereForAI/aya-23-8B | Huggingface          | A100-80GB (Modal) | 1.39 Seconds (Excluding Coldstart Time) |
| CohereForAI/aya-23-35B | Huggingface          | 2xA100-80GB (Modal) | 2.04 Seconds (Excluding Coldstart Time) |
| CohereForAI/c4ai-command-r-plus-4bit | Huggingface          | A100-80GB (Modal) | ToDo |
| CohereForAI/c4ai-command-r-plus | Huggingface          | A100-80GB (Modal) | ToDo |
| CohereForAI/c4ai-command-r-v01-4bit | Huggingface          | A100-80GB (Modal) | ToDo |
| CohereForAI/c4ai-command-r-v01 | Huggingface          | A100-80GB (Modal) | ToDo |

