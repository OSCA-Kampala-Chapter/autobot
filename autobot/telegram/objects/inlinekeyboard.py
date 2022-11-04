from .base import BaseObject
from . import InlineKeyboardButton, WebAppInfo, LoginUrl
from typing import List, Optional
class InlineKeyboardMarkup(BaseObject):

    """"
    
        This object represents an inline keyboard that appears right next to the message it belongs to.

        Args:

            inline_keyboard (List[:obj:`InlineKeyboardButton`]) : Array of button rows, each represented by an Array of InlineKeyboardButton objects
    
    """
    
    __slots__ = ("inline_keyboard",)

    def __init__(self, inline_keyboard: List[InlineKeyboardButton]) -> None:
        self.inline_keyboard = inline_keyboard

class InlineKeyboardButton(BaseObject):

    """"
    
        This object represents one button of an inline keyboard. You must use exactly one of the optional fields.

        Args:
            text (str) : Label text on the button

            url	 (str) : Optional. HTTP or tg:// URL to be opened when the button is pressed. 
            Links tg://user?id=<user_id> can be used to mention a user by their ID without using a username, 
            if this is allowed by their privacy settings.

            callback_data (str) : Optional. Data to be sent in a callback query to the bot when button is pressed, 1-64 bytes

            web_app (:obj:`WebAppInfo`) : Optional. Description of the Web App that will be launched when the user presses the button. 
            The Web App will be able to send an arbitrary message on behalf of the user using the method answerWebAppQuery. 
            Available only in private chats between a user and the bot.

            login_url (:obj:`LoginUrl`) : Optional. An HTTPS URL used to automatically authorize the user. 
            Can be used as a replacement for the Telegram Login Widget.

            switch_inline_query (str) : Optional. If set, pressing the button will prompt the user to select one of their chats, 
            open that chat and insert the bot's username and the specified inline query in the input field. May be empty, 
            in which case just the bot's username will be inserted.

                Note: This offers an easy way for users to start using your bot in inline mode when they are currently in a private chat with it. 
                Especially useful when combined with switch_pm… actions - in this case the user will be automatically returned to the chat they switched from, 
                skipping the chat selection screen.

            switch_inline_query_current_chat (str) : Optional. If set, pressing the button will insert the bot's username and the specified inline query 
            in the current chat's input field. May be empty, in which case only the bot's username will be inserted.

                This offers a quick way for the user to open your bot in inline mode in the same chat - good for selecting something from multiple options.

            callback_game (:obj:`CallbackGame`) : Optional. Description of the game that will be launched when the user presses the button.

                Note: This type of button must always be the first button in the first row.

            pay (bool) : Optional. Specify True, to send a Pay button.

                Note: This type of button must always be the first button in the first row and can only be used in invoice messages.

    """
    
    __slots__ = (
                "url",
                "callback_data",
                "web_app",
                "login_url",
                "switch_inline_query",
                "switch_inline_query_current_chat",
                "callback_game",
                "pay",
                )

    def __init__(self, text:str):
        self.text = text
        self.url: Optional[str] = None
        self.callback_data: Optional[str] = None
        self.web_app: Optional[WebAppInfo] = None
        self.login_url: Optional[LoginUrl] = None
        self.switch_inline_query: Optional[str] = None
        self.switch_inline_query_current_chat: Optional[str] = None
        self.callback_game: Optional[str] = None
        self.pay: Optional[bool] = None
