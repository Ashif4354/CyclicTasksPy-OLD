from lib import CyclicTasks
from aiohttp import ClientSession
from asyncio import run
from dotenv import load_dotenv

load_dotenv()

async def main():
    async with ClientSession() as session:
        print("\n Cyclic Tasks is running...\n")
        CT = CyclicTasks(session)
        await CT.start()

if __name__ == "__main__":
    print("\n Cyclic Tasks is running...\n")
    run(main())
        
