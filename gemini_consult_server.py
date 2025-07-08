import os
from typing import Dict, Any
from fastmcp import FastMCP
from google import genai

mcp = FastMCP(name="Gemini Consultation Server")
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
MODEL_NAME = os.environ["GEMINI_MODEL"]

@mcp.tool
async def collaborative_problem_solving(problem_statement: str, claude_solution: str) -> Dict[str, Any]:
    """Consult Gemini when debugging attempts fail. 
    
    Args:
        problem_statement: The bug/error you're trying to fix
        claude_solution: What approaches you've already tried that didn't work
    """
    prompt = f"""Problem: {problem_statement}

Claude's proposed solution:
{claude_solution}

Please review this solution and provide:
1. Strengths of the approach
2. Potential issues or improvements
3. Alternative approaches to consider
4. Specific recommendations for the next iteration"""

    try:
        response = await client.aio.models.generate_content(model=MODEL_NAME, contents=prompt)
        return {"status": "success", "response": response.text}
    except Exception as e:
        return {"status": "error", "error": str(e)}

if __name__ == "__main__":
    mcp.run()