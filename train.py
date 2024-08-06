from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
import wandb


model = AutoModelForSequenceClassification.from_pretrained("norsu/ai-detector-test")
tokenizer = AutoTokenizer.from_pretrained("microsoft/deberta-v3-base")

wandb.login()

run_name = input("Enter run-name: ")
wandb.init(run_name)
