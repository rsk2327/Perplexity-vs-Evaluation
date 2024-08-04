# Without Chat Template - 

## Multi Line Command -

```
lm_eval --model hf \
    --model_args pretrained='/NS/llm-1/nobackup/afkhan/Model_Saves/aya-23-8B' \
    --tasks 'hellaswag' \
    --device cuda:0 \
    --batch_size auto \
    --write_out \
    --seed 42 \
    --output_path /NS/llm-1/work/afkhan/Perplexity-vs-Evaluation/Experiments/LMEvalHarness_Runs/aya-23-8b-hellaswag_without_template \
    --log_samples \
    --wandb_args project=PPL_vs_Eval,name=aya-23-8b-hellaswag_without_template >> /NS/llm-1/work/afkhan/Perplexity-vs-Evaluation/Experiments/LMEvalHarness_Runs/Logs/aya-23-8b-hellaswag_without_template.log
```

## One Liner Command - 

```
lm_eval --model hf --model_args pretrained='/NS/llm-1/nobackup/afkhan/Model_Saves/aya-23-8B' --tasks 'hellaswag' --device cuda:0 --batch_size auto --write_out --seed 42 --output_path /NS/llm-1/work/afkhan/Perplexity-vs-Evaluation/Experiments/LMEvalHarness_Runs/aya-23-8b-hellaswag_without_template --log_samples --wandb_args project=PPL_vs_Eval,name=aya-23-8b-hellaswag_without_template >> /NS/llm-1/work/afkhan/Perplexity-vs-Evaluation/Experiments/LMEvalHarness_Runs/Logs/aya-23-8b-hellaswag_without_template.log
```

# With Chat Template - 
Broken currently, to use this route see `fix_aya_23_for_lm_eval_harness.ipynb`  

## Multi Line Command -

```
lm_eval --model hf \
    --model_args pretrained='/NS/llm-1/nobackup/afkhan/Model_Saves/aya-23-8B',use_chat_template=True \
    --tasks 'hellaswag' \
    --device cuda:0 \
    --batch_size auto \
    --write_out \
    --seed 42 \
    --output_path /NS/llm-1/work/afkhan/Perplexity-vs-Evaluation/Experiments/LMEvalHarness_Runs/aya-23-8b-hellaswag_with_template \
    --log_samples \
    --wandb_args project=PPL_vs_Eval,name=aya-23-8b-hellaswag_with_template >> /NS/llm-1/work/afkhan/Perplexity-vs-Evaluation/Experiments/LMEvalHarness_Runs/Logs/aya-23-8b-hellaswag_with_template.log
```

## One Liner Command - 

```
lm_eval --model hf --model_args pretrained='/NS/llm-1/nobackup/afkhan/Model_Saves/aya-23-8B' --apply_chat_template --tasks 'hellaswag' --device cuda:1 --batch_size auto --write_out --seed 42 --output_path /NS/llm-1/work/afkhan/Perplexity-vs-Evaluation/Experiments/LMEvalHarness_Runs/aya-23-8b-hellaswag_with_template --log_samples --wandb_args project=PPL_vs_Eval,name=aya-23-8b-hellaswag_with_template >> /NS/llm-1/work/afkhan/Perplexity-vs-Evaluation/Experiments/LMEvalHarness_Runs/Logs/aya-23-8b-hellaswag_with_template.log
```
