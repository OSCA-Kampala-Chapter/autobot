from ..objects import BaseObject

class InlineQuery(BaseObject):
    
    __slots__ = ("id",
                "from_",
                "query",
                "offset",
                "chat_type",
                "location",
                )
    def __init__(self,id,from_,query,offset):
        self.id = id
        self.from_ = from_
        self.query = query
        self.offset = offset
        self.chat_type = None
        self.location = None
        
class InlineQueryResult (BaseObject):
    """
    Base class for InlineQueryResult* objects.
    """
    __slots__ = ("type",
                "id",
                )
    def __init__ (self,type,id):
        self.type = type
        self.id = id
        
