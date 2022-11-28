"""
This module contains the runner and scheduler base classes
The runner maintains and schedules the execution of tasks
on the event loop via the scheduler
"""

import asyncio
import time
from autobot.events.dispatcher import EventDispatcher

class Scheduler:
    """
    Scheduler base class
    """
    
class Runner (Scheduler,EventDispatcher):
    """
    Runner base class
    """