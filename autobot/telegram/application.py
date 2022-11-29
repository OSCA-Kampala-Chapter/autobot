"""
This module contains the telegram application class
"""
import asyncio
from autobot.events.dispatcher import EventDispatcher
from autobot.events import Event
from autobot.telegram.context import Context,MessageBox


class Application (EventDispatcher):

    def __init__ (self,
        token,
        context = None,
        **kwargs
    ):
        self.context = context if context else Context(token,dispatcher = self)
        self.highest_update_id = 0
        super(Application,self).__init__(**kwargs)
        self.register_event("Update")

    async def run_polling (self):             #Add parameters to customize the loop and get_updates call
        """
        Poll the bot for updates
        """
        updates = await self.context.get_updates()
        await self._handle_updates(updates)

        while True:
            next_update = self.highest_update_id + 1
            updates = await self.context.get_updates(offset = next_update)
            await self._handle_updates(updates)

    async def _handle_updates (self,updates):
        event = Event("Update")
        for update in updates:
            if ((upid := update.update_id) >= self.highest_update_id):
                self.highest_update_id = upid
            event.event_value = MessageBox(update,self.context)
            await self.dispatch(event)

    def start_polling (self):
        """
        Run the application
        """
        asyncio.run(self.run_polling())