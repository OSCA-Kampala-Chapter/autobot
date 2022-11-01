from ..objects import BaseObject

class Game (BaseObject):

    __slots__ = ("title",
                "description",
                "photo",
                "text",
                "text_entities",
                "animation",
                )
    def __init__ (self,title,description,photo):
        self.title = title
        self.description = description
        self.photo = photo
        self.text = None
        self.text_entities = None
        self.animation = None
        
        
class GameHighScore (BaseObject):
    
    __slots__ = ("position",
                "user",
                "score",
                )
    def __init__ (self,position,user,score):
        self.position = position
        self.user = user
        self.score = score
        