import asyncio
from mcp.server import fifaclient
from mcp.claude_bridge import claudebridge

class ChatInterface:
    def __init__(self):
        self.client = WC26Client()
        self.bridge = None
    
    async def start(self):
        
        try:
            await self.client.connect()
            self.bridge = claudebridge(self.client)
            
            
            print("Type your questions about World Cup 2026")
            print("Type 'quit' to exit\n")
            
            tools = await self.client.get_tools()
            print(f"Access to {len(tools)} MCP tools\n")
            
            while True:
                question = input("You: ").strip()
                
                if question.lower() == "quit":
                    print("\nbye")
                    break
                
                if not question:
                    continue
                
                print("\nAgent: Thinking...")
                response = await self.bridge.ask_question(question)
                print(f"Agent: {response}\n")
        
        except Exception as e:
            print(f"Error: {e}")
        
        finally:
            await self.client.disconnect()
           
    
    async def run(self):
       
        await self.start()