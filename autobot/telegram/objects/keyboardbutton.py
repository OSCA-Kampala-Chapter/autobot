from .base import BaseObject

class KeyboardButton(BaseObject):
    def __init__(self,
        type,
        request_contact = None,
        request_location = None,
        request_poll = None,
        web_app = None
        ):

        self.type = type
        self.request_contact = request_contact
        self.request_location = request_location
        self.request_poll = request_poll
        self.web_app = web_app



class KeyboardButtonPollType(BaseObject):
    def __init__(self, type = None):
        self.type = type

