from autobot.telegram.objects.base import BaseObject
from typing import Optional

class File(BaseObject):
    """
    This object represents a file ready to be downloaded.

    Args:
        file_id (str): Unique identifier for this file

        file_unique_id (str): Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
        
        file_size (int): Optional. File size, if known
        
        file_path (str): Optional. File path. Use https://api.telegram.org/file/bot<token>/<file_path> to get the file.
    """

    
    
    def __init__(self, file_id:str = None, file_unique_id:str = None) -> None:
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.file_size: Optional[int] = None
        self.file_path: Optional[str] = None
        

