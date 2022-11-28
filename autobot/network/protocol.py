"""
The Protocol module contains abstract classes that represent a protocol.
The Classes expose specific methods that define the relevant protocol
and can be used to send and receive requests. 
The Concrete subclasses should implement the given methods
"""
from typing import Protocol
from abc import abstractmethod

class HTTP (Protocol):
    """
    Base abstraction class for the HTTP Protocol
    """

    @abstractmethod
    async def get (self,url:str,headers:dict = None) -> dict:
        """
        abstract get method
        """

    @abstractmethod
    async def post (self,url:str,headers:dict = None,body:dict = None) -> dict:
        """
        abstract post method
        """

    @abstractmethod
    async def close (self):
        """
        abstract close method
        """

class WebSocket:
    """
    Base abstraction class for the Websocket protocol
    """