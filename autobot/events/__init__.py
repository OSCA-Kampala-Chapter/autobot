"""
The events system of autobot contains 
1) The Event
2) The Dispatcher
3) The Processor
4) The Runner
5) The Scheduler

The event system is also back-pressured and implements a 
custom back-pressure protocol centered around state of the processor
"""

class OverLoadedError(Exception):
    """
    raised by the processor once it is overloaded
    """