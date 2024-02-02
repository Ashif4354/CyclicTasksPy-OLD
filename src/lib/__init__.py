from asyncio import create_task, gather

from .aters_server_pacemaker.aters_server_pacemaker import AtersServerPacemaker
from .self_check_vitals.self_check_vitals import SelfCheckVitals

class CyclicTasks:
    def __init__(self, Session):
        self.Session = Session
        self.tasks = []

    async def start(self):
        await self.add_tasks()
        await gather(*self.tasks)

    async def add_tasks(self):

        #1
        SelfCheckVitalsTask = create_task(SelfCheckVitals(self.Session).pacemake())
        self.tasks.append(SelfCheckVitalsTask)
        
        #2
        AtersServerPacemakerTask = create_task(AtersServerPacemaker(self.Session).pacemake())
        self.tasks.append(AtersServerPacemakerTask)


