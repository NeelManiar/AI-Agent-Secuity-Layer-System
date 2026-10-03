
from datasets import load_dataset

dataset = load_dataset(
    "MLZoo/CrossMCP-Bench",
    data_files="scenarios.jsonl",
    split="train"
)

print(dataset)
print(dataset[0])