from autobot.telegram.objects import BaseObject
from typing import Optional

class ForumTopicCreated (BaseObject):
    """
    This object represents a service message about a new forum topic created in the chat

    <https://core.telegram.org/bots/api#forumtopiccreated>

    Args:
        name: (str) Name of the topic
        icon_color: (int) Color of the topic icon in RGB format
        icon_custom_emoji_id: (str) Optional. Unique identifier of the custom emoji shown as the topic icon
    """

    
    def __init__(self, name: str = None, icon_color: int = None) -> None:
        self.name = name
        self.icon_color = icon_color
        self.icon_custom_emoji_id: Optional[str] = None
        
class ForumTopicClosed (BaseObject):
    """
    This object represents a service message about a forum topic closed in the chat. Currently holds no information.
    """
    pass
    
class ForumTopicReopened (BaseObject):
    """
    This object represents a service message about a forum topic reopened in the chat. Currently holds no information.
    """
    pass