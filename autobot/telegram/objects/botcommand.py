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
    pass 

class BotCommandScopeAllGroupChats(BaseObject):
    pass 

class BotCommandScopeAllPrivateChats(BaseObject):
    pass
    
class BotCommandScopeChat(BaseObject):
    pass 

class BotCommandScopeChatAdministrators(BaseObject):
    pass 

class BotCommandScopeChatMember(BaseObject):
    pass 

class BotCommandScopeDefault(BaseObject):
    pass 
