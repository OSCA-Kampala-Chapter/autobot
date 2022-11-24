from autobot.telegram.objects.base import BaseObject
from autobot.telegram.objects.photosize import PhotoSize
from autobot.telegram.objects.user import User
from typing import Optional

class Video(BaseObject):
    """
    This object represents a video file.

    Args:
        file_id (str): Unique identifier for this file
        file_unique_id (str): Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
        width (int): Video width as defined by sender
        height (int): Video height as defined by sender
        duration (int): Duration of the video in seconds as defined by sender
        thumb (:class:`telegram.objects.photo_size.PhotoSize`): Optional. Video thumbnail
        mime_type (str): Optional. Mime type of a file as defined by sender
        file_size (int): Optional. File size
    """


    
    def __init__(self, file_id: str = None, file_unique_id: str = None, width: int = None, height: int = None, duration: int = None) -> None:
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.duration = duration
        self.thumb: Optional[PhotoSize] = None
        self.mime_type: Optional[str] = None
        self.file_size: Optional[int] = None
    
class VideoChatEnded(BaseObject):
    """
    This object represents a service message about a video chat ended in the chat.
    
        Args:
            duration (int): Video duration in seconds
    """
    
    __slots__ = ("duration",)
    
    def __init__(self, duration: int = None) -> None:
        self.duration = duration
    
class VideoChatParticipantsInvited(BaseObject):
    """
    This object represents a service message about new members invited to a video chat.

    Args:
        users (list[:class:`telegram.objects.user.User`]): Optional. New members that were invited to the video chat
    """
    
    __slots__ = ("users",)
    
    def __init__(self, users: list[User] = None) -> None:
        self.users = users

    
class VideoChatScheduled(BaseObject):
    """
    This object represents a service message about a video chat scheduled in the chat.
    
        Args:
            start_date (:class:`telegram.objects.base.UnixTime`): Point in time (Unix timestamp) when the video chat is supposed to be started by a chat administrator
    """
    
    __slots__ = ("start_date",)
    
    def __init__(self, start_date: int = None) -> None:
        self.start_date = start_date

    
class VideoChatStarted(BaseObject):
    #This object represents a service message about a video chat started in the chat. 
    #
    #Currently holds no information.
    pass

    
class VideoNote(BaseObject):
    """
    This object represents a video message (available in Telegram apps as of v.4.0).

    Args:
        file_id (str): Unique identifier for this file
        file_unique_id (str): Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
        length (int): Video width and height (diameter of the video message) as defined by sender
        duration (int): Duration of the video in seconds as defined by sender
        thumb (:class:`telegram.objects.photo_size.PhotoSize`): Optional. Video thumbnail
        file_size (int): Optional. File size
    """

    __slots__ = (
        'file_id',
        'file_unique_id',
        'length',
        'duration',
        'thumb', 
        'file_size'
        )

    
    def __init__(self, file_id: str = None, file_unique_id: str = None, length: int = None, duration: int = None) -> None:
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.length = length
        self.duration = duration
        self.thumb: Optional[PhotoSize] = None
        self.file_size: Optional[int] = None
  
