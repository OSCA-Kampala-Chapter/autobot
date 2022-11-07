from .base import BaseObject
from . import WebAppInfo

class MenuButton(BaseObject):
    
    """
        This object describes the bot's menu button in a private chat. It should be one of
        MenuButtonCommands
        MenuButtonWebApp
        MenuButtonDefault
        If a menu button other than MenuButtonDefault is set for a private chat, then it is applied in the chat. 
        Otherwise the default menu button is applied. By default, the menu button opens the list of bot commands.
    """


class MenuButtonCommands(BaseObject):
    
    """
        Represents a menu button, which opens the bot's list of commands.
        Args: 
            type (str) : Type of the button, must be commands
    """ 

    __slots__ = ("type",)

    def __init__(self, type: str) -> None:
        self.type = type


class MenuButtonWebApp(BaseObject):
    
     
    """
        Represents a menu button, which launches a Web App.
        Args: 
            type (str) : Type of the button, must be web_app
            text (str) : Text on the button
            web_app (:obj :`WebAppInfo`) : Description of the Web App that will be launched when the user presses the button. 
            The Web App will be able to send an arbitrary message on behalf of the user using the method answerWebAppQuery.
    """ 

    __slots__ = (
        "type", 
        "text", 
        "web_app",
        )

    def __init__(self, type: str, text: str, web_app: WebAppInfo) -> None:
        self.type = type
        self.text = text
        self.web_app = web_app


class MenuButtonDefault(BaseObject):
    
    """
        Describes that no specific value for the menu button was set.
        Args:
            type (str) : Type of the button, must be default
    """

    __slots__ = ("type",)

    def __init__(self, type: str) -> None:
        self.type = type