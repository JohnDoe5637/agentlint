import json
import sys
from collections import Counter

def load_actions(filename):
    actions = []
    with open(filename) as f:
        for number, line in enumerate(f, start=1):
            if line.strip() == "":
                continue
            try:
                actions.append(json.loads(line))
            except json.JSONDecodeError:
                print(f"Bad line {number} in {filename}: {line.strip()!r}")
                sys.exit(1)
    return actions

def find_repeats(actions):
    problems = []
    counts = Counter((a["tool"], json.dumps(a["args"])) for a in actions)
    for (tool, args), n in counts.items():
        if n > 1:
            problems.append(
                f"WASTE: {tool} was called {n} times with the same input {args}"
            )
    return problems

def find_failures(actions):
    problems = []
    for a in actions:
        if a.get("error"):
            problems.append(f"FAILED: {a['tool']} failed with error: {a['error']}")
    return problems

def find_bloat(actions):
    problems = []
    for i in range(1, len(actions)):
        before = actions[i - 1].get("input_tokens")
        now = actions[i].get("input_tokens")
        if before is None or now is None:
            continue
        if now - before > 2000:
            problems.append(
                f"BLOAT: turn {i + 1} input jumped from {before} to {now} tokens"
            )
    return problems
    
def main():
    if len(sys.argv) < 2:
        print("Usage: py agentlint.py <tracefile>")
        sys.exit(1)
    
    actions = load_actions(sys.argv[1])
    problems = find_repeats(actions) + find_failures(actions) + find_bloat(actions)
    
    for p in problems:
        print(p)
    print(f"Found {len(problems)} issues.")
    

if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    

