# agentlint

A command-line tool that reads AI agent logs and flags wasted effort and failures.

## What it detects

1. **WASTE**: the same tool called more than once with the same input
2. **FAILED**: tool calls that returned an error
3. **BLOAT**: input tokens that jump by more than 2000 between turns

## Usage

```
py agentlint.py trace.jsonl
```

## Example output

```
WASTE: search was called 3 times with the same input {"q": "weather"}
FAILED: fetch_page failed with error: timeout
FAILED: fetch_page failed with error: 404
BLOAT: turn 4 input jumped from 700 to 5000 tokens
BLOAT: turn 6 input jumped from 5200 to 9000 tokens
Found 5 issues.
```

## Log format

One JSON object per line:

```
{"tool": "search", "args": {"q": "weather"}, "input_tokens": 500}
```

Optional field: `"error": "timeout"`

## Files

1. `agentlint.py`: the tool
2. `trace.jsonl`: sample log with problems
3. `clean.jsonl`: sample log with no problems
