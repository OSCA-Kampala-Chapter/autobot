from autobot.telegram.objects.base import BaseObject
from typing import Optional

class PhotoSize(BaseObject):
    """This object represents one size of a photo or a file / sticker thumbnail.

    Args:
        file_id (str) : Identifier for this file, which can be used to download or reuse the file

        file_unique_id (str) : Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.

        width (int) : Video width 

        height (int) : Video height 

        file_size (int) : Optional. File size in bytes
    """

    __slots__ = ("file_id",
                "file_unique_id",
                "width",
                "height",
                "file_size",
                )

    def __init__(self, 
                file_id:str = None,
                file_unique_id:str = None, 
                width:str = None, 
                height:str = None
                ):
                
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.file_size: Optional[int] = None

 
