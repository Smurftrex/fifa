import asyncio
from cli.chat import ChatInterface
async def main():
    
    chat = ChatInterface()
    await chat.run()

if __name__ == "__main__":
    asyncio.run(main())