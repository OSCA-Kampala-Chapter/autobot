from __future__ import annotations
from autobot.telegram.objects.base import BaseObject
from typing import Optional, TYPE_CHECKING


if TYPE_CHECKING:
    from autobot.telegram.objects.message import Message
    from autobot.telegram.objects.user import User
    from autobot.telegram.objects.location import Location

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


    def __init__(self, id: int = None, type: str = None) -> None:
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
    """
    This object represents the rights of a chat administrator.
    
    Refer to the `Telegram API documentation <https://core.telegram.org/bots/api#chatadministrator>`_ for more information.

    Args:
        is_anonymous	(bool):	True, if the user's presence in the chat is hidden
        can_manage_chat	(bool):	True, if the administrator can access the chat event log, chat statistics, message statistics in channels, see channel members, see anonymous administrators in supergroups and ignore slow mode. Implied by any other administrator privilege
        can_delete_messages	(bool):	True, if the administrator can delete messages of other users
        can_manage_video_chats (bool):	True, if the administrator can manage video chats
        can_restrict_members (bool):	True, if the administrator can restrict, ban or unban chat members
        can_promote_members	(bool):	True, if the administrator can add new administrators with a subset of their own privileges or demote administrators that he has promoted, directly or indirectly (promoted by administrators that were appointed by the user)
        can_change_info	(bool):	True, if the user is allowed to change the chat title, photo and other settings
        can_invite_users (bool): True, if the user is allowed to invite new users to the chat
        can_post_messages (bool): Optional. True, if the administrator can post in the channel; channels only
        can_edit_messages (bool): Optional. True, if the administrator can edit messages of other users and can pin messages; channels only
        can_pin_messages (bool): Optional. True, if the user is allowed to pin messages; groups and supergroups only
        can_manage_topics (bool): Optional. True, if the user is allowed to create, rename, close, and reopen forum topics; supergroups only
    """


    def __init__(self, is_anonymous: bool = None, can_manage_chat: bool = None, can_delete_messages: bool = None, can_manage_video_chats: bool = None, can_restrict_members: bool = None, can_promote_members: bool = None, can_change_info: bool = None, can_invite_users: bool = None) -> None:
        self.is_anonymous: Optional[bool] = is_anonymous
        self.can_manage_chat: Optional[bool] = can_manage_chat
        self.can_delete_messages: Optional[bool] = can_delete_messages
        self.can_manage_video_chats: Optional[bool] = can_manage_video_chats
        self.can_restrict_members: Optional[bool] = can_restrict_members
        self.can_promote_members: Optional[bool] = can_promote_members
        self.can_change_info: Optional[bool] = can_change_info
        self.can_invite_users: Optional[bool] = can_invite_users
        self.can_post_messages: Optional[bool] = None
        self.can_edit_messages: Optional[bool] = None
        self.can_pin_messages: Optional[bool] = None
        self.can_manage_topics: Optional[bool] = None
    
class ChatInviteLink(BaseObject):
    """
    This object represents an invite link for a chat.
    
    Refer to the `Telegram API documentation <https://core.telegram.org/bots/api#chatinvitelink>`_ for more information.

    Args:
        invite_link (str): The invite link. If the link was created by another chat administrator, then the second part of the link will be replaced with “…”.
        creator (User): Creator of the link
        is_primary (bool): True, if the link is primary
        is_revoked (bool): True, if the link is revoked
        expire_date (int): Optional. Point in time (Unix timestamp) when the link will expire or has been expired
        member_limit (int): Optional. Maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999
    """


    def __init__(self, invite_link: str = None, creator: User = None, is_primary: bool = None, is_revoked: bool = None) -> None:
        self.invite_link: Optional[str] = invite_link
        self.creator: Optional[User] = creator
        self.is_primary: Optional[bool] = is_primary
        self.is_revoked: Optional[bool] = is_revoked
        self.expire_date: Optional[int] = None
        self.member_limit: Optional[int] = None
    
class ChatJoinRequest(BaseObject):
    """
    This object represents a chat member that has joined the chat by an invite link.
    
    Refer to the `Telegram API documentation <https://core.telegram.org/bots/api#chatjoinrequest>`_ for more information.

    Args:
        user (User): User that requested to join the chat
        status (str): Optional. The member's status in the chat. Can be “creator”, “administrator”, “member”, “restricted”, “left” or “kicked”
    """


    def __init__(self, user: User = None) -> None:
        self.user: Optional[User] = user
        self.status: Optional[str] = None
    
class ChatLocation(BaseObject):
    """
    This object represents a location to which a chat is connected.
    
    Refer to the `Telegram API documentation <https://core.telegram.org/bots/api#chatlocation>`_ for more information.

    Args:
        location (Location): The location to which the supergroup is connected. Can't be a live location.
        address (str): Location address; 1-64 characters, as defined by the chat owner
    """


    def __init__(self, location: Location = None, address: str = None) -> None:
        self.location: Optional[Location] = location
        self.address: Optional[str] = address
    
class ChatPermissions(BaseObject):
    """
    This object describes actions that a non-administrator user is allowed to take in a chat.
    
    Refer to the `Telegram API documentation <https://core.telegram.org/bots/api#chatpermissions>`_ for more information.

    Args:
        can_send_messages (bool): Optional. True, if the user is allowed to send text messages, contacts, locations and venues
        can_send_media_messages (bool): Optional. True, if the user is allowed to send audios, documents, photos, videos, video notes and voice notes, implies can_send_messages
        can_send_polls (bool): Optional. True, if the user is allowed to send polls, implies can_send_messages
        can_send_other_messages (bool): Optional. True, if the user is allowed to send animations, games, stickers and use inline bots, implies can_send_media_messages
        can_add_web_page_previews (bool): Optional. True, if the user is allowed to add web page previews to their messages, implies can_send_media_messages
        can_change_info (bool): Optional. True, if the user is allowed to change the chat title, photo and other settings. Ignored in public supergroups
        can_invite_users (bool): Optional. True, if the user is allowed to invite new users to the chat
        can_pin_messages (bool): Optional. True, if the user is allowed to pin messages. Ignored in public supergroups
    """


    def __init__(self) -> None:
        self.can_send_messages: Optional[bool] = None
        self.can_send_media_messages: Optional[bool] = None
        self.can_send_polls: Optional[bool] = None
        self.can_send_other_messages: Optional[bool] = None
        self.can_add_web_page_previews: Optional[bool] = None
        self.can_change_info: Optional[bool] = None
        self.can_invite_users: Optional[bool] = None
        self.can_pin_messages: Optional[bool] = None

    
class ChatPhoto(BaseObject):
    """
    This object represents a chat photo.
    
    Refer to the `Telegram API documentation <https://core.telegram.org/bots/api#chatphoto>`_ for more information.

    Args:
        small_file_id (str): Unique file identifier of small (160x160) chat photo. This file_id can be used only for photo download.
        small_file_unique_id (str): Unique file identifier of small (160x160) chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
        big_file_id (str): Unique file identifier of big (640x640) chat photo. This file_id can be used only for photo download.
        big_file_unique_id (str): Unique file identifier of big (640x640) chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    """


    def __init__(self, small_file_id: str = None, small_file_unique_id: str = None, big_file_id: str = None, big_file_unique_id: str = None) -> None:
        self.small_file_id: Optional[str] = small_file_id
        self.small_file_unique_id: Optional[str] = small_file_unique_id
        self.big_file_id: Optional[str] = big_file_id
        self.big_file_unique_id: Optional[str] = big_file_unique_id

