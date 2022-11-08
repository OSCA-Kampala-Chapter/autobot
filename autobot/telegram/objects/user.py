from autobot.telegram.objects.base import BaseObject
from autobot.telegram.objects.photosize import PhotoSize
from typing import Optional

class User(BaseObject):
    """
    This object represents a Telegram user or bot.
        
        Args:
            id (int): Unique identifier for this user or bot
            is_bot (bool): True, if this user is a bot
            first_name (str): User's or bot's first name
            last_name (Optional[str]): Optional. User's or bot's last name
            username (Optional[str]): Optional. User's or bot's username
            language_code (Optional[str]): Optional. IETF language tag of the user's language
            can_join_groups (Optional[bool]): Optional. True, if the bot can be invited to groups. Returned only in getMe.
            can_read_all_group_messages (Optional[bool]): Optional. True, if privacy mode is disabled for the bot. Returned only in getMe.
            supports_inline_queries (Optional[bool]): Optional. True, if the bot supports inline queries. Returned only in getMe.
        """
    
    __slots__ = (
            'id',
            'is_bot',
            'first_name',
            'last_name', 
            'username', 
            'language_code', 
            'can_join_groups', 
            'can_read_all_group_messages', 
            'supports_inline_queries'
            )
        
        
    def __init__(self, id: int = None, is_bot: bool = None, first_name: str = None) -> None:
        self.id = id
        self.is_bot = is_bot
        self.first_name = first_name
        self.last_name: Optional[str] = None
        self.username: Optional[str] = None
        self.language_code: Optional[str] = None
        self.can_join_groups: Optional[bool] = None
        self.can_read_all_group_messages: Optional[bool] = None
        self.supports_inline_queries: Optional[bool] = None

         



class UserProfilePhotos(BaseObject):
    """
    This object represent a user's profile pictures.

    Args:
        total_count (int): Total number of profile pictures the target user has
        photos (List[List[PhotoSize]]): Requested profile pictures (in up to 4 sizes each)
    """

    __slots__ = (
        'total_count', 
        'photos'
        )

    def __init__(self, total_count: int = None, photos: list[list[PhotoSize]] = None) -> None:
        self.total_count = total_count
        self.photos = photos
