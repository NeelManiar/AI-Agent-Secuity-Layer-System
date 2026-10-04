
import json
from pathlib import Path

RAW_FILE = Path("data/raw/crossmcp_scenarios.jsonl")
OUTPUT_FILE = Path("data/scenarios.json")

def load_scenarios():
    scenarios = []

    with RAW_FILE.open("r") as f:
        for line in f:
            line = line.strip()

            if line:
                scenarios.append(json.loads(line))

    return scenarios

def normalize_scenario(scenario):
    auth_context = json.loads(scenario["auth_context"])
    expected_tools = json.loads(scenario["expected_tools"])

    return {
        "id": scenario["id"],

        "context": {
            "authorization": auth_context,
            "user_instruction": scenario["user_instruction"],
            "sensitivity": scenario["sensitivity_label"],
            "tools": expected_tools,
        },

        "ground_truth": {
            "is_attack": scenario["is_attack"],
            "attack_type": scenario["attack_type"],
            "expected_policy": scenario["expected_policy"],
        }
    }

def main():
    scenarios = load_scenarios()

    normalized = [
        normalize_scenario(scenario)
        for scenario in scenarios
    ]

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_FILE.open('w') as f:
        json.dump(normalized,f, indent=2)

    print(f'Loaded {len(scenarios)} scenarios')


if __name__ == '__main__':
    main()