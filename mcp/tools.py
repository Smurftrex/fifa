import json

class ToolHandler:
    def __init__(self, client):
        self.client = client

    async def get_available_tools(self):
        tools = await self.client.get_tools()
        return [{"name": tool.name, "description": tool.description} for tool in tools]
    async def execute_tool(self, tool_name, arguments):
        
        try:
            result = await self.client.call_tool(tool_name, arguments)
            return result
        except Exception as e:
            return f"Error executing tool: {str(e)}"
    def format_tools_for_claude(self, tools):
        
        tool_list = "\n".join([f"- {tool['name']}: {tool['description']}" for tool in tools])
        return tool_list