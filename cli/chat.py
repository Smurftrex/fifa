import asyncio
from mcp.client import fifaclient
class ChatInterface:
    def __init__(self):
        self.client = fifaclient()

    async def start(self):
        try:
            await self.client.connect()
            tools = await self.client.get_tools()
            print(f"Available tools: {len(tools)}\n")
            while True:
                question = input("You: ").strip()
                if question.lower() == "quit":
                    print("bye")
                    break
                
                if not question:
                    continue
                
                print(f"\Processing\n")
                # We'll add actual tool calling next
                
        except Exception as e:
            print(f"Error: {e}")
        
        finally:
            await self.client.disconnect()
    async def run(self):
        
        await self.start()
