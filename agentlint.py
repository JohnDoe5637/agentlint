import json
import sys
from collections import Counter

if len(sys.argv) < 2:
    print("Usage: py agentlint.py <tracefile>")
    sys.exit(1)

filename = sys.argv[1]

actions = []
with open(filename) as f:
    for line in f:
        if line.strip() == "":
            continue
        actions.append(json.loads(line))

issues = 0

# Detector 1: repeated calls
counts = Counter((a["tool"], json.dumps(a["args"])) for a in actions)

for (tool, args), n in counts.items():
    if n > 1:
        print(f"WASTE: {tool} was called {n} times with the same input {args}")
        issues += 1

# Detector 2: failed calls
for a in actions:
    if a.get("error"):
        print(f"FAILED: {a['tool']} failed with error: {a['error']}")
        issues += 1

# Detector 3: context bloat
for i in range(1, len(actions)):
    before = actions[i - 1].get("input_tokens")
    now = actions[i].get("input_tokens")
    if before is None or now is None:
        continue
    if now - before > 2000:
        print(f"BLOAT: turn {i + 1} input jumped from {before} to {now} tokens")
        issues += 1

print(f"Found {issues} issues.")