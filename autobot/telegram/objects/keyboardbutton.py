from autobot.telegram.objects.base import BaseObject
from typing import Optional

class KeyboardButton(BaseObject):
    """
   This object represents one button of the reply keyboard. 
   For simple text buttons String can be used instead of 
   this object to specify text of the button. 
   Optional fields `web_app`, `request_contact`, `request_location`, 
   and `request_poll` are mutually exclusive..

    Args:
        text (str): Text of the button. If none of the optional fields are used, it will be sent as a message when the button is pressed
        type (str): Type of the button. Must be one of: text, request_contact, request_location, request_poll, web_app
        request_contact (bool): Optional. If True, the user's phone number will be sent as a contact when the button is pressed. Available in private chats only
        request_location (bool): Optional. If True, the user's current location will be sent when the button is pressed. Available in private chats only
        request_poll (str): Optional. If specified, the user will be asked to create a poll and send it to the bot when the button is pressed. Available in private chats only
        web_app (str): Optional. If specified, the user will be asked to create a poll and send it to the bot when the button is pressed. Available in private chats only
"""

    
    def __init__(self, text: str = None, type: str = None) -> None:
        self.text = text
        self.type = type
        self.request_contact: Optional[bool] = None
        self.request_location: Optional[bool] = None
        self.request_poll: Optional[str] = None
        self.web_app: Optional[str] = None



class KeyboardButtonPollType(BaseObject):
    """
    This object represents type of a poll, which is allowed to be created 
    and sent when the corresponding button is pressed.

    Args:
        type (str): Optional. If quiz is passed, the user will be allowed to create only polls in the quiz mode. 
        If regular is passed, only regular polls will be allowed. Otherwise, the user will be allowed to create a poll of any type.
    """


    def __init__(self, type: str = None) -> None:
        self.type = type

