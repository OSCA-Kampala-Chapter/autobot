from ..objects import BaseObject, PhotoSize, MessageEntity, User, Animation
from typing import Optional

class Game(BaseObject):
    
    __slots__ = ("title",
                "description",
                "photo",
                "text",
                "text_entities",
                "animation",
                )

    def __init__(self, title: str, description: str, photo: list[PhotoSize]) -> None:
        self.title = title
        self.description = description
        self.photo = photo
        self.text: Optional[str] = None
        self.text_entities: Optional[list[MessageEntity]] = None
        self.animation: Optional[Animation] = None


class GameHighScore(BaseObject):

    __slots__ = ("position",
                "user",
                "score",
                )


    def __init__(self, position: int, user: User, score: int) -> None:
        self.position = position
        self.user = user
        self.score = score     



        