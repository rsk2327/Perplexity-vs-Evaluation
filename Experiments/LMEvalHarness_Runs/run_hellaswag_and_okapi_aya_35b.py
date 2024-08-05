import os

os.environ["HF_HOME"] = "/NS/llm-1/nobackup/afkhan/HF_CACHE/Misc"
os.environ["HF_DATASETS_CACHE"] = "/NS/llm-1/nobackup/afkhan/HF_CACHE/Datasets"
os.environ["TRANSFORMERS_CACHE"] = "/NS/llm-1/nobackup/afkhan/HF_CACHE/Models"

cache_dir = os.getenv("TRANSFORMERS_CACHE")

import argparse

arg_parser = argparse.ArgumentParser()

arg_parser.add_argument("--apply_chat_template", default="")

args = arg_parser.parse_args()

apply_chat_template = args.apply_chat_template

chat_template = False

if apply_chat_template == 'Yes':
    chat_template = True
elif apply_chat_template == 'No':
    chat_template = False
else:
    raise ValueError("Invalid value for apply_chat_template")

task_prepend = "hellaswag"
tasks = "ar,bn,ca,da,de,es,eu,fr,gu,hi,hr,hu,hy,id,it,kn,ml,mr,ne,nl,pt,ro,ru,sk,sr,sv,ta,te,uk,vi"
task_list = list(tasks.split(","))
TASKS = [task_prepend + "_" + task for task in task_list]
TASKS.append("hellaswag")

if chat_template:
    run_command = f"""lm_eval --model hf --model_args pretrained='/NS/llm-1/nobackup/afkhan/Model_Saves/aya-23-35B' --apply_chat_template --tasks {','.join(TASKS)} --batch_size auto --write_out --seed 42 --output_path /NS/llm-1/work/afkhan/Perplexity-vs-Evaluation/Experiments/LMEvalHarness_Runs/aya-23-35B-hellaswag_with_okapi_with_template --log_samples --wandb_args project=PPL_vs_Eval,name=aya-23-35B-hellaswag_with_okapi_with_template >> /NS/llm-1/work/afkhan/Perplexity-vs-Evaluation/Experiments/LMEvalHarness_Runs/Logs/aya-23-35B-hellaswag_with_okapi_with_template.log"""
else:
    run_command = f"""lm_eval --model hf --model_args pretrained='/NS/llm-1/nobackup/afkhan/Model_Saves/aya-23-35B' --tasks {','.join(TASKS)} --batch_size auto --write_out --seed 42 --output_path /NS/llm-1/work/afkhan/Perplexity-vs-Evaluation/Experiments/LMEvalHarness_Runs/aya-23-35B-hellaswag_with_okapi_without_template --log_samples --wandb_args project=PPL_vs_Eval,name=aya-23-35B-hellaswag_with_okapi_without_template >> /NS/llm-1/work/afkhan/Perplexity-vs-Evaluation/Experiments/LMEvalHarness_Runs/Logs/aya-23-35B-hellaswag_with_okapi_without_template.log"""

print(run_command)

os.system(run_command)