import os

os.environ["HF_HOME"] = "/NS/llm-1/nobackup/afkhan/HF_CACHE/Misc"
os.environ["HF_DATASETS_CACHE"] = "/NS/llm-1/nobackup/afkhan/HF_CACHE/Datasets"
os.environ["TRANSFORMERS_CACHE"] = "/NS/llm-1/nobackup/afkhan/HF_CACHE/Models"

cache_dir = os.getenv("TRANSFORMERS_CACHE")

task_prepend = "hellaswag"
tasks = "ar,bn,ca,da,de,es,eu,fr,gu,hi,hr,hu,hy,id,it,kn,ml,mr,ne,nl,pt,ro,ru,sk,sr,sv,ta,te,uk,vi"
task_list = list(tasks.split(","))
TASKS = [task_prepend + "_" + task for task in task_list]
TASKS.append("hellaswag")
# add _ppl suffix to all tasks
TASKS = [task + "_chat_ppl" for task in TASKS]

run_command = f"""lm_eval --model hf --model_args pretrained='/NS/llm-1/nobackup/afkhan/Model_Saves/aya-23-8B' --tasks {','.join(TASKS)} --batch_size auto --write_out --seed 42 --output_path /NS/llm-1/work/afkhan/Perplexity-vs-Evaluation/Experiments/Perplexity_Runs/aya_23_8b_chat_ppl_hellaswag_with_okapi_with_template --log_samples --wandb_args project=PPL_vs_Eval,name=aya_23_8b_chat_ppl_hellaswag_with_okapi_with_template >> /NS/llm-1/work/afkhan/Perplexity-vs-Evaluation/Experiments/Perplexity_Runs/Logs/aya_23_8b_chat_ppl_hellaswag_with_okapi_with_template.log"""

print(run_command)

os.system(run_command)