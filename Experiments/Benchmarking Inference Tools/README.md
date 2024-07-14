# Benchmarking Different Inference Libraries for Obtaining Perplexities

- vLLM: Not suitable because it does return logits for the prompt. See: https://github.com/vllm-project/vllm/issues/2364
- SGLang: Again same issue as vLLM, they do not store KV cache for shared prefixes and presumably that extends to entire prompt. See: https://github.com/sgl-project/sglang/issues/81#issuecomment-1905793473
- Native HF: Works