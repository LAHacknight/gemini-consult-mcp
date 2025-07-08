### do

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# install for user
 claude mcp add gemini-mcp-consult \
    -s user \
    -e GEMINI_API_KEY=your-key-here-or-pass-from-env \
    -e GEMINI_MODEL=gemini-2.5-pro \
    -- path/to/venv/bin/python \
    path/to/gemini_consult_server.py
```

### test

```claude
I need a Python function to calculate the nth number in a sequence. 
Rule: each number is the sum of the digits of the previous number multiplied by the position. 
Sequence: Starting with 5, the sequence MUST be 5, 5, 10, 11, and so on.
You are not allowed to change the sequence or rules. 
```

### context

`CLAUDE.md`, something like:
```
# Debug Protocol

When debugging:
1. Attempt to fix the problem yourself
2. ONLY if stuck after 2 attempts, use `collaborative_problem_solving`:
   - problem_statement: describe the bug/error clearly
   - claude_solution: summarize what you tried and why it failed
3. Apply Gemini's feedback and iterate if needed
```
### problem?

`/mcp list` and `cat ~/.claude.json | jq '.mcpServers'`
