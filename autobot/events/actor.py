"""
This mdoule contains the processor machinery used to implement the producers and consumers
of the events. The processors have an associated queue that accepts and contains events
to be processed.
"""
from __future__ import annotations

import asyncio
import types
from typing import Any,TYPE_CHECKING
from collections.abc import Callable
from autobot.events import OverLoadedError
from autobot.events import Event

EVENT_VALUE = Any

if TYPE_CHECKING:
    from autobot.events.dispatcher import EventDispatcher

__all__ = ("Actor")

class EventManager(asyncio.Queue):
    """
    Handles the buffering of events received from the event dispatcher
    """

    def __init__ (self,max_size = 0):
        super(EventManager,self).__init__(max_size)


    async def dispatch_hook (self) -> None:
        """
        method used to listen and pick up events from the dispatcher
        """
        
        while True:
            relay = self._relay()

            try:
                event = await relay
                self.put_nowait(event)
            except asyncio.QueueFull:
                raise OverLoadedError
            else:
                await self.schedule_run()

            break

    @types.coroutine
    def _relay (self):
        """
        An internal method used to capture the event from the dispatcher
        and pass it over to the dispatch hook for consumption
        """
        message = None
        while True:
            message = yield message
            return message

    async def schedule_run(self) -> None:
        """
        Schedule the action to run on the event loop
        """
        event_loop = asyncio.get_running_loop()
        task = event_loop.create_task(self.run())
        await task

    async def task_done(self) -> None:
        """
        Notify that task is done and suspend the action
        """
        super().task_done()
        await asyncio.sleep(0)

    get_task = _relay



class Actor (EventManager):
    """
    Base class for an event handler
    """

    def __init__ (self,*,
        queue_size:int = 0,
        dispatcher:EventDispatcher = None
        ):

        super(Actor,self).__init__(queue_size)
        self.dispatcher = dispatcher if dispatcher else self._get_dispatcher()

    def _get_dispatcher (self):
        """
        Used to get the central event dispatcher from the runner 
        """
        try:
            event_loop = asyncio.get_running_loop()
            return event_loop.central_dispatcher
        except:
            return None


    def run_in_background (func:Callable[...,Any]):
        """
        Run a blocking synchronous operation in a background thread.
        It is a wrapper around the asyncio.to_thread function
        """
        async def async_runner (*args,**kwargs):
            result = await asyncio.to_thread(func,*args,**kwargs)
            return result

        return async_runner


    async def action (self):
        """
        The action method should be implemented by the BaseActor subclass.
        """
        raise NotImplementedError("Actor action is not implemented")

    async def run (self):
        """
        Get event from the task manager and pass its value to the action method
        for processing.
        """

        action = self.action()
        action.send(None)
        while True:

            try:
                event = self.get_nowait()
            except asyncio.QueueEmpty:
                break
            else:
                action.send(event.event_value)

        action.close()

    async def call_dispatcher(self,event:Event) -> None:
        """
        Call a dispatcher to dispatch an event to its listeners
        """
        await self.dispatcher.dispatch(event)