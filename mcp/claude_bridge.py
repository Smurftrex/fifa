import requests
import json
from config.settings import ANTHROPIC_API_KEY
from mcp.tools import ToolHandler

class ClaudeBridge:
    def __init__(self, client):
        self.client = client
        self.tool_handler = ToolHandler(client)
        self.api_key = ANTHROPIC_API_KEY
    async def ask_question(self, question):
        try:
           
            tools = await self.tool_handler.get_available_tools()
            tools_description = self.tool_handler.format_tools_for_claude(tools)

            response = requests.post(
                "https://api.anthropic.com/v1/messages",
                headers={
                    "Content-Type": "application/json",
                    "x-api-key": self.api_key
                },
                json={
                    "model": "claude-sonnet-4-6",
                    "max_tokens": 2000,
                    "system": f"""You are a World Cup 2026 expert .
                    You have access to these MCP tools:
                    {tools_description}

                    help answer questions about World Cup 2026 using these tools.
                    Be conversational and helpful""",
                    "messages": [
                        {"role": "user", "content": question}
                    ]
                }
            )
            if response.status_code == 200:
                data = response.json()
                if "content" in data and len(data["content"]) > 0:
                    return data["content"][0]["text"]
                return "No response received"
            else:
                return f"Error: {response.status_code} - {response.text}"
        except Exception as e:
            return f"Error: {str(e)}"