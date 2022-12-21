"""
This module contains the Event Dispatcher.
The event dispatcher is responsible for receiving events and distributing
them to the registered listeners
"""

from __future__ import annotations

import asyncio
import types
from collections.abc import Coroutine,Callable
from typing import Any
from inspect import iscoroutine
from collections import deque
from autobot.events import OverLoadedError
from autobot.events.events import Event


ID = int
EVENT_NAME = str

__all__ = ("EventDispatcher")

"""
The most number of events that a single dispatcher should be able to 
monitor and dispatch. Ideally this should not be changed.
"""
MAX_EVENTS_HARD_LIMIT = 30

class HardLimitExceededError (ValueError):
    """
    Exception raised when the hard limit is exceed
    """
class LimitExceededError (ValueError):
    """
    Exception raised when the current limit of events in an event dispatcher
    is exceeded
    """
class EventNotRegistered (Exception):
    """
    Exception raised when trying to listen to an event that doesnot exist in
    the dispatcher. This is only triggered when strict_mode is True
    """


class ProcState:
    """
    A container for the processor that helps us monitor its health
    and helps participate in the backpressure protocol
    """

    def __init__ (self,listener:Coroutine) -> None:

        self.pending_events = deque()
        self.listener = None
        try:
            listener.send(None)
        except:
            if not iscoroutine(listener):
                raise ValueError(f"<{listener}> is not a coroutine")
            raise ValueError(f"<{listener}> failed to initialize")
        else:
            self.listener = listener

   
    async def call (self) -> None:

        while True:

            try:
                event = self.pending_events.popleft()
            except IndexError:
                break
            else:
                try:
                    self.listener.send(event)
                except OverLoadedError:
                    self.pending_events.appendleft(event)
                    task = asyncio.create_task(self.resume_pending())
                    await task
                except StopIteration:
                    break
            
    async def resume_pending (self):
        
        try:
            self.process_pending()
        except OverLoadedError:
            task = asyncio.create_task(self.resume_pending())
            await task

    def process_pending (self):
        try:
            while (event := self.pending_events.popleft()):
                self.listener.send(event)
        except IndexError:
            return


class _EventProxy:
    """
    A proxy to moderate the access to the event listeners table.
    Contains the methods to interact with the internal listeners table.
    """
    def __init__ (self):

        self.__event_listeners = {}     # listeners table
        self.__max_events = 0
        self.__strict_mode = False


    def _set_event_handler (self,val:tuple[EVENT_NAME,ID,Coroutine]) -> None:
        """
        Set a function to hanlde this event
        """
        _event, _callback_id, _callback = val
        if (self._events_number() <= self._max_events):
            pass
        else:
            raise LimitExceededError("number of events registered in dispatcher has exceeded the current maximum")

        if (self._strict_mode and _event not in self._event_listeners):
            raise EventNotRegistered(f"event <{_event}> is not registered in dispatcher")
        try:
            self._event_listeners[_event] |= {_callback_id:_callback}
        except KeyError:
            self._event_listeners[_event] = {_callback_id:_callback}
        
    def _events_number (self):
        return len(self._event_listeners)
    
    @property
    def _max_events (self):
        return self.__max_events

    @_max_events.setter
    def _max_events (self,val):
        val = abs(val)
        if (val > MAX_EVENTS_HARD_LIMIT):
            raise HardLimitExceededError(f"{val} greater than events limit")
        self.__max_events = val

    @property
    def _strict_mode (self):
        return self.__strict_mode

    @_strict_mode.setter
    def _strict_mode (self,val:bool):
        if not isinstance(val,bool):
            raise ValueError (f"{val} should be of type {bool}")
        self.__strict_mode = val

    @property
    def _event_listeners (self):
        return self.__event_listeners

    def _register (self,event_type) -> None:

        if (self._events_number() <= self._max_events):
            pass
        else:
            raise LimitExceededError("number of events registered in dispatcher has exceeded the current maximum")
        
        if event_type in self._event_listeners:
            pass
        else:
            self._event_listeners[event_type] = {}

    def _is_registered(self,event:EVENT_NAME) -> bool:

        return event in self.__event_listeners

    def _all_event_listeners (self):

        return [name for name in self.__event_listeners]

    def __repr__ (self):
        return self.__event_listeners.__repr__()

    def __str__ (self) -> str:
        return self.__repr__()

class EventDispatcher:

    def __init__ (self,*,
        strict_mode = False,
        max_events = 10
        ):

        self.listeners = _EventProxy()
        self.listeners._strict_mode = strict_mode
        self.listeners._max_events = max_events

    def events_number (self):
        """
        the number of events that the dispatcher is currently monitoring
        """
        
        return self.listeners._events_number()


    @property
    def max_events (self):
        """
        the current maximum number of events the dispatcher can monitor
        """

        return self.listeners._max_events

    @max_events.setter
    def max_events (self,val):
        self.listeners._max_events = val

    @property
    def strict_mode (self):
        """
        attribute to control if listen should automatically add the event to event dispatcher
        or not. Default value is False, True will cause the event dispatcher to raise an error
        if listen is trying to listen to an event that is not yet registered to the event
        dispatcher
        """
        return self.listeners._strict_mode

    @strict_mode.setter
    def strict_mode (self,val:bool) -> None:
        self.listeners._strict_mode = val

    def add_listener (self,
        event_type:EVENT_NAME, 
        callback:Coroutine
        ) -> ID:
        """
        add a listener callback which listens to a specific even. The callback
        should take in a single event as a parameter and return immediately with 
        the current state of the processor
        """
        callback_id = id(callback)
        self.listeners._set_event_handler((event_type,callback_id,ProcState(callback)))
        return callback_id

    def remove_listener(self,
        event_type:EVENT_NAME,
        listener_id:ID
        ) -> None:
        """
        remove the listener with id listener_id from listeners table
        """
        try:
           listener_table = self.listeners._event_listeners[event_type]
        except KeyError:
            raise EventNotRegistered(f"event <{event_type}> is not registered in dispatcher")
        else:
            try:
                listener_table.pop(listener_id)
            except KeyError:
                raise AttributeError(f"listener of id <{listener_id}> not found")


    def register_event (self,event:EVENT_NAME) -> None:
        """
        Register an event to the dispatcher
        """
        self.listeners._register(event)

    def is_registered (self,event:EVENT_NAME) -> bool:
        """
        check is event is registered
        """
        return self.listeners._is_registered(event)

    def all_event_listeners (self):
        """
        return a list of all registered events
        """
        return self.listeners._all_event_listeners()

    async def dispatch (self,event:Event) -> None:
        """
        distribute the event among the listeners
        """
        event_type = event.event_type
        try:
            listeners_table = self.listeners._event_listeners[event_type]
        except KeyError:
            raise EventNotRegistered(f"event <{event_type}> is not registered in dispatcher")
        else:
            for listener in listeners_table.values():
                listener.pending_events.append(event)
            await self._dispatch(listeners_table)

    async def _dispatch (self,table:dict):

        for listener in table.values():
            await listener.call()

    def __repr__ (self):
        return self.__class__.__name__

    def __str__ (self):
        return self.listeners.__repr__()

    @types.coroutine
    def _relay (self):
        """
        A relay generator used to capture the values fron send and pass it back to the
        coroutine
        """
        msg = None
        while True:
            msg = yield msg
            return msg


    def add_handler (self,event_name:EVENT_NAME):
        self.register_event(event_name)

        def prepare_handler (async_func):
            async def async_func_decorator ():
                while True:
                    relay = self._relay()
                    ent_val = await relay
                    await async_func(ent_val)

            callback_id = self.add_listener(event_name,async_func_decorator())
            return callback_id
        
        return prepare_handler


    def run_in_background (func:Callable[...,Any]):
        """
        Run a blocking synchronous operation in a background thread.
        It is a wrapper around the asyncio.to_thread function
        """
        async def async_runner (*args,**kwargs):
            result = await asyncio.to_thread(func,*args,**kwargs)
            return result

        return async_runner
