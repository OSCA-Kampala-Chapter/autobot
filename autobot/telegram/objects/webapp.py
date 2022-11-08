from autobot.telegram.objects.base import BaseObject

class WebAppData(BaseObject):
    def __init__(self,
        data = None,
        button_text = None,
    ):

        self.data = data
        self.button_text = button_text


class WebAppInfo(BaseObject):
    def __init__(self,
        url: str = None,
    ):
        self.url = url 
