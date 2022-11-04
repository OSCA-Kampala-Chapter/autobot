from .base import BaseObject
from .photosize import PhotoSize
from typing import Optional

class Audio(BaseObject):
    """
    This object represents an audio file to be treated as music by the Telegram clients.

    Args:
        file_id (str): Unique identifier for this file
        
        file_unique_id (str): Unique identifier for this file, which is supposed to be the same over time and for different bots. 
        Can't be used to download or reuse the file.
        
        duration (int): Optional Duration of the audio in seconds as defined by sender
        
        performer (str): Optional. Performer of the audio as defined by sender or by audio tags
        
        title (str): Optional. Title of the audio as defined by sender or by audio tags
        
        file_name (str): Optional. Original filename as defined by sender
        
        mime_type (str): Optional. MIME type of the file as defined by sender
        
        file_size (int): Optional. File size
        
        thumb (:obj:`PhotoSize`, optional): Optional. Thumbnail of the album cover to which the music file belongs
    """

    __slots__ = (
        'duration', 
        'performer', 
        'title', 
        'file_name', 
        'mime_type', 
        'file_size', 
        'thumb'
    )

    def __init__(self, file_id, file_unique_id):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.duration: Optional[int] = None
        self.performer: Optional[str] = None
        self.title: Optional[str] = None
        self.file_name: Optional[str] = None
        self.mime_type: Optional[str] = None
        self.file_size: Optional[int] = None
        self.thumb: Optional[PhotoSize] = None

