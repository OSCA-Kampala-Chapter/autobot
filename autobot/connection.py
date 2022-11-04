from typing import Protocol
from abc import abstractmethod
import httpx

__all__ = ("Connection","Connector")

class Connection (Protocol):
    """
    Base class for the Connector object. It provides
    two methods `get` and `post` which should be implemented
    by the concrete classes
    """
    
    @abstractmethod
    def get (self,url,header,body):
        raise NotImplementedError
     
    @abstractmethod
    def post (self,url,header,body):
        raise NotImplementedError
        
        
class Connector (Connection):
    pass
    
