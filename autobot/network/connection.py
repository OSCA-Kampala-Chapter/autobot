"""
This module contains specific implementations for the abstract protocols in the
protocol module. The protocols are implemented as connection classes. This module uses
httpx to implement the protocol api
"""

import httpx
from autobot.network.protocol import HTTP

class HTTPConnection(HTTP):

    def __init__ (self):
        
        self.client = httpx.AsyncClient()

    async def get (self,url:str,headers:dict = None) -> dict:
        """
        concrete implementation of get
        """
        if headers:
            response = await self.client.get(url,headers = headers)
        response = await self.client.get(url)
        return response.content


    async def post (self,url:str,headers:dict = None,body:dict = None) -> dict:
        """
        concrete implementation of post
        """
        if body:
            if headers:
                response = await self.client.post(url,headers = headers, data = body)
            response = await self.client.post(url,params = body)
        return response.content

    async def close (self):
        """
        concrete implementation of close
        """
        await self.client.aclose()
