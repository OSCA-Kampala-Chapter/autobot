"""
This module contains the representation of an event.
An event is represented as a class with two main public attributes, that is,
the type attribute to specify the type of event,
and the param attribute to capture the details of the event
"""
__all__ = ("Event")


class Event:
    
    __slots__ = ("event_type","event_values")
    
    def __init__ (self,event_type:str = None, event_values:tuple = None):
        self.event_type = event_type
        self.event_values = event_values