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

## Future Improvements

AgentLint is an early-stage project focused on identifying inefficiencies in AI agent execution logs. The goal is to develop it into a more comprehensive debugging and performance analysis tool.

Potential improvements include:

- **Performance metrics:** Track total tool calls, failure rates, and estimated token usage across agent runs.
- **Cost analysis:** Estimate API costs based on token consumption and model pricing.
- **Duplicate detection:** Improve detection of redundant tool calls, including requests with slightly different inputs.
- **Reporting:** Generate structured JSON and HTML reports summarizing detected issues.
- **Visualization:** Build a dashboard for comparing agent performance across multiple runs.
- **Automated testing:** Add unit tests to verify detection accuracy across different log formats.

## Project Goals

The long-term objective is to make debugging AI agents easier by automatically identifying unnecessary operations, failed tool calls, and inefficient context usage.

AgentLint is built with Python and designed to be lightweight, easy to run, and adaptable to different agent logging systems.

## Features

- Analyze code for potential issues
- Identify areas for improvement
- Provide clear, actionable feedback
