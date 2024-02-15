from lib import CyclicTasks
from aiohttp import ClientSession
from asyncio import run
from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return jsonify({'message': 'Cyclic Tasks is running...'})

async def main():
    async with ClientSession() as session:
        print("\n Cyclic Tasks is running...\n")
        CT = CyclicTasks(session)
        await CT.start()

if __name__ == "__main__":
    print("\n Cyclic Tasks is running...\n")
    run(main())
        
