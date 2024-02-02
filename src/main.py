from lib import CyclicTasks
from aiohttp import ClientSession
from asyncio import run
from dotenv import load_dotenv

load_dotenv()

async def main():
    async with ClientSession() as session:
        CT = CyclicTasks(session)
        await CT.start()

if __name__ == "__main__":
    run(main())
        
