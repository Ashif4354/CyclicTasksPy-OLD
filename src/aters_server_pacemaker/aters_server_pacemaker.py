from asyncio import sleep
from os import getenv
from datetime import datetime

class AtersServerPacemaker:
    def __init__(self, Session):
        self.Session = Session

    async def get_aters(self):
        try:
            response = await self.Session.get('https://aters-server.onrender.com/')
            print(await response.text())
            await self.send_discord_webhook()
            response.close()
        except Exception as e:
            print('Failed to get aters server', e) 
    
    async def send_discord_webhook(self):
        url = getenv('DISCORD_WEBHOOK_URL_CYCLIC_TASKS_PY')

        headers = {
            'Content-Type': 'application/json'
        }

        data = {
            'embeds': [
                {
                    'title': 'Aters Server Pacemaker',
                    'description': f'Made sure server stays alive by sending one pulse at : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}',
                    'color': 0x0066ff
                }
            ]
        }

        try:
            await self.Session.post(url, json=data, headers=headers)
        except Exception as e:
            print('Failed to send discord webhook in AtersServerPacemaker\n', e)

    async def pacemake(self):
        while True:
            await self.get_aters()
            await sleep(60)
    
