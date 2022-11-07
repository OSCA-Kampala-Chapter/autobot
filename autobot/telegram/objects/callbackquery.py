from __future__ import annotations
from .base import BaseObject
from .user import User
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .message import Message

class CallBackQuery(BaseObject):
    """
    This object represents an incoming callback query from a callback button in an inline keyboard. If the button that originated the query was attached to a message sent by the bot, the field message will be present. If the button was attached to a message sent via the bot (in inline mode), the field inline_message_id will be present. Exactly one of the fields data or game_short_name will be present.
    
    Args:
        id (str): Unique identifier for this query
        from (telegram.objects.user.User): Sender
        message (Optional[telegram.objects.message.Message]): Optional. Message with the callback button that originated the query. Note that message content and message date will not be available if the message is too old
        inline_message_id (Optional[str]): Optional. Identifier of the message sent via the bot in inline mode, that originated the query.
        chat_instance (str): Global identifier, uniquely corresponding to the chat to which the message with the callback button was sent. Useful for high scores in games.
        data (Optional[str]): Optional. Data associated with the callback button. Be aware that a bad client can send arbitrary data in this field.
        game_short_name (Optional[str]): Optional. Short name of a Game to be returned, serves as the unique identifier for the game
    """

    __slots__ = (
        'id',
        'from',
        'message',
        'inline_message_id',
        'chat_instance',
        'data',
        'game_short_name'
    )

    def __init__(self, id: str, from_: User, chat_instance: str):
        self.id = id
        self.from_ = from_
        self.chat_instance = chat_instance
        self.message: Optional[Message] = None
        self.inline_message_id: Optional[str] = None
        self.data: Optional[str] = None
        self.game_short_name: Optional[str] = None


