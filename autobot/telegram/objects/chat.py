from __future__ import annotations
from .base import BaseObject
from typing import Optional, TYPE_CHECKING


if TYPE_CHECKING:
    from .message import Message

class Chat(BaseObject):
    """
    This object represents a chat.

    Args:
        id (int): Unique identifier for this chat. This number may be greater than 32 bits and some programming languages may 
        have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or 
        double-precision float type are safe for storing this identifier.
        type (str): Type of chat, can be either “private”, “group”, “supergroup” or “channel”
        title (str): Optional. Title, for supergroups, channels and group chats
        username (str): Optional. Username, for private chats, supergroups and channels if available
        first_name (str): Optional. First name of the other party in a private chat
        last_name (str): Optional. Last name of the other party in a private chat
        all_members_are_administrators (bool): Optional. True if a group has ‘All Members Are Admins’ enabled.
        photo (:obj:`ChatPhoto`, optional): Optional. Chat photo. Returned only in getChat.
        description (str): Optional. Description, for supergroups and channel chats. Returned only in getChat.
        invite_link (str): Optional. Chat invite link, for supergroups and channel chats. Returned only in getChat.
        pinned_message (:obj:`Message`, optional): Optional. Pinned message, for supergroups and channel chats. Returned only in getChat.
        sticker_set_name (str): Optional. For supergroups, name of group sticker set. Returned only in getChat.
        can_set_sticker_set (bool): Optional. True, if the bot can change the group sticker set. Returned only in getChat.
        linked_chat_id (int): Optional. The minimum allowed delay between consecutive messages sent by each unpriviledged user. Returned only in getChat.
        location (:obj:`ChatLocation`, optional): Optional. Default chat member permissions, for groups and supergroups. Returned only in getChat.
        bio (str): Optional. A description for the group, shown on the group’s profile page. Returned only in getChat.
        has_private_forwards (bool): Optional. True, if the group has a discussion group for administrators. Returned only in getChat.
        has_restricted_voice_and_video_messages (bool): Optional. True, if the group has a discussion group for administrators. Returned only in getChat.
        join_to_send_messages (bool): Optional. True, if the group has a discussion group for administrators. Returned only in getChat.
        join_by_request (bool): Optional. True, if the group has a discussion group for administrators. Returned only in getChat.
        permissions (:obj:`ChatPermissions`, optional): Optional. True, if the group has a discussion group for administrators. Returned only in getChat.
        slow_mode_delay (int): Optional. True, if the group has a discussion group for administrators. Returned only in getChat.
        message_auto_delete_time (int): Optional. True, if the group has a discussion group for administrators. Returned only in getChat.
    """

    __slots__ = (
        'id',
        'type',
        'title',
        'username',
        'first_name',
        'last_name',
        'all_members_are_administrators',
        'photo',
        'description',
        'invite_link',
        'pinned_message',
        'sticker_set_name',
        'can_set_sticker_set',
        'linked_chat_id',
        'location',
        'bio',
        'has_private_forwards',
        'has_restricted_voice_and_video_messages',
        'join_to_send_messages',
        'join_by_request',
        'permissions',
        'slow_mode_delay',
        'message_auto_delete_time',
        'has_protected_content'

    )

    def __init__(self, id: int, type: str) -> None:
        self.id = id
        self.type = type
        self.title: Optional[str] = None
        self.username: Optional[str] = None
        self.first_name: Optional[str] = None
        self.last_name: Optional[str] = None
        self.all_members_are_administrators: Optional[bool] = None
        self.photo: Optional[ChatPhoto] = None
        self.description: Optional[str] = None
        self.invite_link: Optional[str] = None
        self.pinned_message: Optional[Message] = None
        self.sticker_set_name: Optional[str] = None
        self.can_set_sticker_set: Optional[bool] = None
        self.linked_chat_id: Optional[int] = None
        self.location: Optional[ChatLocation] = None
        self.bio: Optional[str] = None
        self.has_private_forwards: Optional[bool] = None
        self.has_restricted_voice_and_video_messages: Optional[bool] = None
        self.join_to_send_messages: Optional[bool] = None
        self.join_by_request: Optional[bool] = None
        self.permissions: Optional[ChatPermissions] = None
        self.slow_mode_delay: Optional[int] = None
        self.message_auto_delete_time: Optional[int] = None




    
class ChatAdministratorRights(BaseObject):
    pass
    
class ChatInviteLink(BaseObject):
    pass
    
class ChatJoinRequest(BaseObject):
    pass
    
class ChatLocation(BaseObject):
    pass
    
class ChatPermissions(BaseObject):
    pass
    
class ChatPhoto(BaseObject):
    pass