from typing import Optional

from autobot.telegram.objects import BaseObject


class ForumTopic(BaseObject):
    
    def __init__(self, message_thread_id: int = None, name:str = None, icon_color:int=None) -> None:
        
        __slots__  = (
            "message_thread_id",
            "name",
            "icon_color",
            "icon_custom_emoji_id"
        )
        """This object represents a forum topic.

        Args:
            message_thread_id (int): Unique identifier of the forum topic
            name (str): Name of the topic
            icon_color (int): Color of the topic icon in RGB format
            icon_custom_emoji_id (str, Optional): Unique identifier of the custom emoji shown as the topic icon
        """
        self.message_thread_id = message_thread_id
        self.name = name
        self.icon_custom_emoji_id: Optional[str] = None 
        
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