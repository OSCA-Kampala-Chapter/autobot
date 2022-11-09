from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from autobot.telegram.objects.base import BaseObject

if TYPE_CHECKING:
    from autobot.telegram.objects.user import User
    from autobot.telegram.objects.chat import Chat, ChatInviteLink

class ChatMember(BaseObject):
    """
    This object contains information about one member of a chat. Currently, the following 6 types of chat members are supported:
    * ChatMemberOwner
    * ChatMemberAdministrator
    * ChatMemberMember
    * ChatMemberRestricted
    * ChatMemberLeft
    * ChatMemberBanned
    """
    
class ChatMemberAdministrator(BaseObject):
    """
    Represents a chat member that has some additional privileges.

    <https://core.telegram.org/bots/api#chatmemberadministrator>

    Args:
        status (:obj:`str`): The member's status in the chat, always “administrator”.
        user (:obj:`User`): Information about the user.
        custom_title (:obj:`str`): Optional Custom title for this user.
        can_be_edited (:obj:`bool`): True, if the administrator can access the chat event log, chat statistics, message statistics in channels, see channel members, see anonymous administrators in supergroups and ignore slow mode. Implied by any other administrator privilege.
        can_manage_chat (:obj:`bool`): True, if the administrator can create channel posts, channels only.
        can_post_messages (:obj:`bool`): Optional True, if the administrator can post in the channel; channels only
        can_edit_messages (:obj:`bool`): Optional True, if the administrator can edit messages of other users and can pin messages; channels only.
        can_delete_messages (:obj:`bool`): True, if the administrator can delete messages of other users.
        can_manage_voice_chats (:obj:`bool`): True, if the administrator can manage voice chats.
        can_restrict_members (:obj:`bool`): True, if the administrator can restrict, ban or unban chat members.
        can_promote_members (:obj:`bool`): True, if the administrator can add new administrators with a subset of his own privileges or demote administrators that he has promoted, directly or indirectly (promoted by administrators that were appointed by the user).
        can_change_info (:obj:`bool`): True, if the administrator can change chat title, photo and other settings.
        can_invite_users (:obj:`bool`): True, if the administrator can invite new users to the chat.
        can_pin_messages (:obj:`bool`): Optional True, if the administrator can pin messages; groups and supergroups only.
        can_manage_topics (:obj:`bool`): Optional True, if the administrator can manage chat threads; only for supergroups.
        is_anonymous (:obj:`bool`): True, if the administrator's presence in the chat is hidden.
    """

    __slots__ = (
        "status",
        "user",
        "custom_title",
        "is_anonymous",
        "can_be_edited",
        "can_manage_chat",
        "can_post_messages",
        "can_edit_messages",
        "can_delete_messages",
        "can_manage_voice_chats",
        "can_restrict_members",
        "can_promote_members",
        "can_change_info",
        "can_invite_users",
        "can_pin_messages",
        "can_manage_topics",
    )

    def __init__(self, status: str = None, user: User = None, can_be_edited: bool = None, can_manage_chat: bool = None, can_delete_messages: bool = None, can_manage_voice_chats: bool = None, can_restrict_members: bool = None, can_promote_members: bool = None, can_change_info: bool = None, can_invite_users: bool = None, is_anonymous: bool = None) -> None:
        self.status = status
        self.user = user
        self.is_anonymous = is_anonymous
        self.can_be_edited = can_be_edited
        self.can_manage_chat = can_manage_chat
        self.can_delete_messages = can_delete_messages
        self.can_manage_voice_chats = can_manage_voice_chats
        self.can_restrict_members = can_restrict_members
        self.can_promote_members = can_promote_members
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_post_messages: Optional[bool] = None
        self.can_edit_messages: Optional[bool] = None
        self.can_pin_messages: Optional[bool] = None
        self.custom_title: Optional[str] = None
        self.can_manage_topics: Optional[bool] = None
    
class ChatMemberBanned(BaseObject):
    """
    Represents a chat member that was banned in the chat and can't return to the chat or view chat messages.

    <https://core.telegram.org/bots/api#chatmemberbanned>

    Args:
        status (:obj:`str`): The member's status in the chat, always “kicked”.
        user (:obj:`User`): Information about the user.
        until_date (:obj:`int`): Date when restrictions will be lifted for this user; unix time.
    """

    __slots__ = (
        "status", 
        "user", 
        "until_date"
        )

    def __init__(self, status: str = None, user: User = None, until_date: int = None) -> None:
        self.status = status
        self.user = user
        self.until_date = until_date
class ChatMemberLeft(BaseObject):
    """
    Represents a chat member that isn't currently a member of the chat, but may join it themselves.

    <https://core.telegram.org/bots/api#chatmemberleft>

    Args:
        status (:obj:`str`): The member's status in the chat, always “left”.
        user (:obj:`User`): Information about the user.
    """

    __slots__ = (
        "status", 
        "user"
        )

    def __init__(self, status: str = None, user: User = None) -> None:
        self.status = status
        self.user = user
    
class ChatMemberMember(BaseObject):
    """
    Represents a chat member that isn't currently a member of the chat, but may join it themselves.

    <https://core.telegram.org/bots/api#chatmembermember>

    Args:
        status (:obj:`str`): The member's status in the chat, always “member”.
        user (:obj:`User`): Information about the user.
    """

    __slots__ = (
        "status", 
        "user"
        )

    def __init__(self, status: str = None, user: User = None) -> None:
        self.status = status
        self.user = user
    
class ChatMemberOwner(BaseObject):
    """
    Represents a chat member that owns the chat and has all administrator privileges.

    <https://core.telegram.org/bots/api#chatmemberowner>

    Args:
        status (:obj:`str`): The member's status in the chat, always “creator”.
        user (:obj:`User`): Information about the user.
        is_anonymous (:obj:`bool`): True, if the user's presence in the chat is hidden.
        custom_title (:obj:`str`): Optional Owner's custom title for the chat.
    """

    __slots__ = (
        "status",
        "user",
        "is_anonymous",
        "custom_title",
    )

    def __init__(self, status: str = None, user: User = None, is_anonymous: bool = None) -> None:
        self.status = status
        self.user = user
        self.is_anonymous = is_anonymous
        self.custom_title: Optional[str] = None
    
class ChatMemberRestricted(BaseObject):
    """
    Represents a chat member that has some additional privileges.

    <https://core.telegram.org/bots/api#chatmemberrestricted>

    Args:
        status (:obj:`str`): The member's status in the chat, always “restricted”.
        user (:obj:`User`): Information about the user.
        is_member (:obj:`bool`): True, if the user is a member of the chat at the moment of the request.
        can_change_info (:obj:`bool`): True, if the user is allowed to change the chat title, photo and other settings.
        can_invite_users (:obj:`bool`): True, if the user is allowed to invite new users to the chat.
        can_pin_messages (:obj:`bool`): True, if the user is allowed to pin messages; groups and supergroups only.
        can_send_messages (:obj:`bool`): Optional True, if the user is allowed to send text messages, contacts, locations and venues.
        can_send_media_messages (:obj:`bool`): True, if the user is allowed to send audios, documents, photos, videos, video notes and voice notes, implies can_send_messages.
        can_send_polls (:obj:`bool`): True, if the user is allowed to send polls, implies can_send_messages.
        can_send_other_messages (:obj:`bool`): True, if the user is allowed to send animations, games, stickers and use inline bots, implies can_send_media_messages.
        can_add_web_page_previews (:obj:`bool`): True, if the user is allowed to add web page previews to their messages, implies can_send_media_messages.
        until_date (:obj:`int`): Date when restrictions will be lifted for this user; unix time.
    """

    __slots__ = (
        "status",
        "user",
        "is_member",
        "can_change_info",
        "can_invite_users",
        "can_pin_messages",
        "can_send_messages",
        "can_send_media_messages",
        "can_send_polls",
        "can_send_other_messages",
        "can_add_web_page_previews",
        "until_date",
    )

    def __init__(self, status: str = None, user: User = None, is_member: bool = None, can_change_info: bool = None, can_invite_users: bool = None, can_pin_messages: bool = None, can_send_messages: bool = None, can_send_media_messages: bool = None, can_send_polls: bool = None, can_send_other_messages: bool = None, can_add_web_page_previews: bool = None, until_date: int = None) -> None:
        self.status = status
        self.user = user
        self.is_member = is_member
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_pin_messages = can_pin_messages
        self.can_send_messages = can_send_messages
        self.can_send_media_messages = can_send_media_messages
        self.can_send_polls = can_send_polls
        self.can_send_other_messages = can_send_other_messages
        self.can_add_web_page_previews = can_add_web_page_previews
        self.until_date = until_date
    
class ChatMemberUpdated(BaseObject):
    """
    This object represents changes in the status of a chat member.

    <https://core.telegram.org/bots/api#chatmemberupdated>

    Args:
        chat (:obj:`Chat`): Chat the user belongs to.
        from (:obj:`User`): Performer of the action, which resulted in the change.
        date (:obj:`int`): Date the change was done in Unix time.
        old_chat_member (:obj:`ChatMember`): Previous information about the chat member.
        new_chat_member (:obj:`ChatMember`): New information about the chat member.
        invite_link (:obj:`ChatInviteLink`): Optional Chat invite link, which was used by the user to join the chat; for joining by invite link events only.
    """

    __slots = (
        "chat",
        "from",
        "date",
        "old_chat_member",
        "new_chat_member",
        "invite_link",
    )

    def __init__(self, chat: Chat = None, from_: User = None, date: int = None, old_chat_member: ChatMember = None, new_chat_member: ChatMember = None) -> None:
        self.chat = chat
        self.from_ = from_
        self.date = date
        self.old_chat_member = old_chat_member
        self.new_chat_member = new_chat_member
        self.invite_link: Optional[ChatInviteLink] = None
