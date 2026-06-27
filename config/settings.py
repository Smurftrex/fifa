import os
from dotenv import load_dotenv
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
MCP_SERVER_COMMAND = "npx"
MCP_SERVER_ARGS = ["-y", "wc26-mcp"]
if not ANTHROPIC_API_KEY:
    raise ValueError("KEY not found in .env")
