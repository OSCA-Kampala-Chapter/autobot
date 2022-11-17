from typing import Protocol
from abc import abstractmethod

__all__ = ("BaseChannel","Channel")

class BaseChannel (Protocol):
    """
    Base class for the Channel object. It provides
    two methods `get` and `post` which should be implemented
    by the concrete classes
    """
    
    @abstractmethod
    def get (self):
        raise NotImplementedError
     
    @abstractmethod
    def post (self,resp):
        raise NotImplementedError
        
        
class Channel (BaseChannel):
    pass
    
