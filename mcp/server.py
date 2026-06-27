import asyncio
from mcp.client.session import ClientSession
from mcp.tools.stdio import StdioServerParameters
from config.settings import MCP_SERVER_COMMAND, MCP_SERVER_ARGS


class fifaclient:
    def __init__(self):
        self.session = None
        self.server_params = StdioServerParameters(
            command=MCP_SERVER_COMMAND,
            args=MCP_SERVER_ARGS
        )
    async def connect(self):
        self.session = ClientSession(self.server_params)
        await self.session.__aenter__()
        print("connected to mcp server")
    async def disconnect(self):
         if self.session:
            await self.session.__aexit__(None, None, None)
    async def get_tools(self):
        
        tools = await self.session.list_tools()
        return tools.tools
    async def call_tool(self, tool_name, arguments):
        
        result = await self.session.call_tool(tool_name, arguments)
        return result
    

