"""
This module contains the context of the telegram bot
"""

from autobot.telegram.api import BotAPI
from autobot.telegram.games.api import GamesAPI
from autobot.telegram.inline.api import InlineAPI
from autobot.telegram.passport.api import PassportAPI
from autobot.telegram.payments.api import PaymentsAPI
from autobot.telegram.stickers.api import StickerAPI
from autobot.network.connection import HTTPConnection
from autobot.network.urlmanager import UrlManager
from autobot.telegram.parser import Parser,Composer
import json

class TelegramResultError(Exception):
    """
    raised when telegram returns "ok" as false
    """

class Context(
    BotAPI,
    GamesAPI,
    InlineAPI,
    PassportAPI,
    PaymentsAPI,
    StickerAPI
):
    parser = Parser()

    composer = Composer()

    def __init__ (self,
        token,*,
        connection = None,
        dispatcher = None
    ):
        
        self.dispatcher = dispatcher
        self.url = UrlManager(token)
        self.connection = connection if connection else HTTPConnection()

    async def _get (self,*,url = None,headers = None):
        """
        The _get method adds error handling on top of the abstract get method provided by
        the get method from the HTTPConnection object. If the return value is a success, that is
        it has "ok" as True, then it returns the json string. If "ok" is False, it extracts the 
        description of the failure and raises an error with the description
        """
        res = await self.connection.get(url,headers)
        return self._error_handler(res)

    async def _post (self,*,url = None,headers = None,body = None):
        """
        The _post method adds error handling on top of the abstract get method provided by
        the get method from the HTTPConnection object. If the return value is a success, that is
        it has "ok" as True, then it returns the json string. If "ok" is False, it extracts the 
        description of the failure and raises an error with the description
        """
        res = await self.connection.post(url,headers,body)
        return self._error_handler(res)

    def _error_handler(self,res):
        """
        This function does the actual error handling used in _get and _post
        """
        res = json.loads(res)
        if res["ok"]:
            return res["result"]
        error_code,desc = res["error_code"],res["description"]
        raise TelegramResultError(f"Error Code <{error_code}>:: {desc}")


class MessageBox:
    """
    MessageBox is an object intended to be used for sending messages between
    telegram actors. The Messagebox contains The telegram object being transfered
    and the context object
    """

    def __init__ (self,telegram_object,context):
        
        self.telegram_object = telegram_object
        self.context = context