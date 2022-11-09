from autobot.telegram.objects.base import BaseObject

class BotCommand(BaseObject):
    
    __slots__ = (
        "command",
        "description",
    )
    
    def __init__ (self,command:str = None,description:str = None) -> None:
        self.command = command
        self.description = description

class BotCommandScope(BaseObject):
   
    __slots__ = ("type")
    def __init__ (self,type:str = None) -> None:
        self.type = type

class BotCommandScopeAllChatAdministrators(BaseObject):
    """
    Represents the scope of bot commands, covering all group and supergroup chat administrators.

    <https://core.telegram.org/bots/api#botcommandscopeallchatadministrators>

    Args:
        type (:obj:`str`): Scope type, must be all_chat_administrators.

    """
    
    __slots__ = ("type",)

    def __init__ (self,type:str = None) -> None:
            self.type = type


class BotCommandScopeAllGroupChats(BaseObject):
    """
    Represents the scope of bot commands, covering all group and supergroup chats.

    <https://core.telegram.org/bots/api#botcommandscopeallgroupchats>

    Args:
        type (:obj:`str`): Scope type, must be all_group_chats.

    """
    
    __slots__ = ("type",)

    def __init__ (self,type:str = None) -> None:
            self.type = type

class BotCommandScopeAllPrivateChats(BaseObject):
    """
    Represents the scope of bot commands, covering all private chats.

    <https://core.telegram.org/bots/api#botcommandscopeallprivatechats>

    Args:
        type (:obj:`str`): Scope type, must be all_private_chats.

    """
    
    __slots__ = ("type",)

    def __init__ (self,type:str = None) -> None:
            self.type = type
    
class BotCommandScopeChat(BaseObject):
    """
    Represents the scope of bot commands, covering a specific chat.

    <https://core.telegram.org/bots/api#botcommandscopechat>

    Args:
        type (:obj:`str`): Scope type, must be chat.
        chat_id (:obj:`int`): Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).
    """

    __slots__ = (
        "type",
        "chat_id",
    )    

    def __init__ (self,type:str = None,chat_id:int = None) -> None:
        self.type = type
        self.chat_id = chat_id    

class BotCommandScopeChatAdministrators(BaseObject):
    """
    Represents the scope of bot commands, covering all administrators of a specific group or supergroup chat.

    <https://core.telegram.org/bots/api#botcommandscopechatadministrators>

    Args:
        type (:obj:`str`): Scope type, must be chat_administrators.
        chat_id (:obj:`int`): Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).
    """

    __slots__ = (
        "type",
        "chat_id",
    )    

    def __init__ (self,type:str = None,chat_id:int = None) -> None:
        self.type = type
        self.chat_id = chat_id

class BotCommandScopeChatMember(BaseObject):
    """
    Represents the scope of bot commands, covering a specific member of a group or supergroup chat.

    <https://core.telegram.org/bots/api#botcommandscopechatmember>

    Args:
        type (:obj:`str`): Scope type, must be chat_member.
        chat_id (:obj:`int`): Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).
        user_id (:obj:`int`): Unique identifier of the target user.
    """

    __slots__ = (
        "type",
        "chat_id",
        "user_id",
    )    

    def __init__ (self,type:str = None,chat_id:int = None,user_id:int = None) -> None:
        self.type = type
        self.chat_id = chat_id
        self.user_id = user_id
class BotCommandScopeDefault(BaseObject):
    """
    Represents the default scope of bot commands. Default commands are used if no commands with a narrower scope are specified for the user.

    <https://core.telegram.org/bots/api#botcommandscopedefault>

    Args:
        type (:obj:`str`): Scope type, must be default.
    """

    __slots__ = ("type",)

    def __init__ (self,type:str = None) -> None:
        self.type = type