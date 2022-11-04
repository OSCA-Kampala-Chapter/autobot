from .base import BaseObject

class Voice(BaseObject):
    """
    This object represents a voice note.

    Args:
        file_id (str): Unique identifier for this file
        file_unique_id (str): Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
        duration (int): Duration of the audio in seconds as defined by sender
        mime_type (str): Optional. MIME type of the file as defined by sender
        file_size (int): Optional. File size
    """

    __slots__ = ('file_id',
                'file_unique_id',
                'duration',
                'mime_type',
                'file_size'
                )

    
    def __init__(self, 
                file_id:str, 
                file_unique_id:str, 
                duration:int
                ):

        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.duration = duration
        self.mime_type = None
        self.file_size = None
 
