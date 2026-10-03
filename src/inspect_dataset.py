
import json

with open('data/raw/crossmcp_scenarios.jsonl') as f:
    line = f.readline()
    scenario = json.loads(line)
    print(scenario.keys())

    print(json.dumps(scenario, indent=4))