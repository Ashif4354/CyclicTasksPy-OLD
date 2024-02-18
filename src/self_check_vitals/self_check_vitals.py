from os import getenv
from webbrowser import get
from datetime import datetime
from asyncio import sleep

from ..lib.GetIstTime import get_ist_time

class SelfCheckVitals:
    def __init__(self, Session):
        self.Session = Session

    async def send_discord_webhook(self):
        url = getenv('DISCORD_WEBHOOK_URL_CYCLIC_TASKS_PY')

        headers = {
            'Content-Type': 'application/json'
        }

        data = {
            'embeds': [
                {
                    'title': 'Self Check Vitals',
                    'description': f'I am alive at {get_ist_time()}',
                    'color': 0xffffff
                }
            ]
        }

        await self.Session.post(url, json=data, headers=headers)

    async def pacemake(self):
        while True:
            await self.send_discord_webhook()
            print('Self Check Vitals: I am alive at', get_ist_time())
            await sleep(1800)
