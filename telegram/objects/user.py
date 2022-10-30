from telegram.objects.photosize import PhotoSize
from .base import BaseObject

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
            'last_name', 
            'username', 
            'language_code', 
            'can_join_groups', 
            'can_read_all_group_messages', 
            'supports_inline_queries'
            )
        
        
    def __init__(self, id, is_bot, first_name):
            self.id = id
            self.is_bot = is_bot
            self.first_name = first_name
            self.last_name = None
            self.username = None
            self.language_code = None
            self.can_join_groups = None
            self.can_read_all_group_messages = None
            self.supports_inline_queries = None

         



class UserProfilePhotos(BaseObject):
    """
    This object represent a user's profile pictures.

    Args:
        total_count (int): Total number of profile pictures the target user has
        photos (List[List[PhotoSize]]): Requested profile pictures (in up to 4 sizes each)
    """

    __slots__ = ('total_count', 'photos')

    def __init__(self, total_count, photos):
        self.total_count = total_count
        self.photos = photos

    @classmethod
    def de_json(cls, data, bot):
        if not data:
            return None

        data = super(UserProfilePhotos, cls).de_json(data, bot)

        data['photos'] = [[PhotoSize.de_json(photo, bot) for photo in photo_list] for photo_list in data['photos']]

        return cls(**data)

    def to_dict(self):
        data = super(UserProfilePhotos, self).to_dict()

        data['photos'] = [[photo.to_dict() for photo in photo_list] for photo_list in self.photos]

        return data

    def __reduce__(self):
        return self.__class__, (self.total_count, self.photos)

    def __eq__(self, other):
        return (self.total_count == other.total_count and
                self.photos == other.photos)

    def __hash__(self):
        return hash((self.total_count, self.photos))

    def __str__(self):
        return 'UserProfilePhotos(total_count={self.total_count!r}, photos={self.photos!r})'.format(self=self)

    def __repr__(self):
        return '<{self.__class__.__name__} total_count={self.total_count!r}, photos={self.photos!r}>'.format(self=self)

    def get_file(self, file_id):
        """
        Shortcut for::

            bot.get_file(file_id)

        Args:
            file_id (:obj:`str`): Unique identifier for the target file

        Returns:
            :class:`telegram.File`: On success, a file object is returned.

        Raises:
            :class:`telegram.TelegramError`

        """
        return self.bot.get_file(file_id)

    def download(self, file_path, filename=None, **kwargs):
        """
        Shortcut for::

            bot.download_file(file_path, filename, **kwargs)

        Args:
            file_path (:obj:`str`): File identifier to get info about
            filename (:obj:`str`, optional): The name of the file. If not set, the file_id will be used.
            **kwargs (:obj:`dict`): Arbitrary keyword arguments.

        Returns:
            :obj:`str`: The file path of the downloaded file.

        Raises:
            :class:`telegram.TelegramError`

        """
        return self.bot.download_file(file_path, filename, **kwargs)
