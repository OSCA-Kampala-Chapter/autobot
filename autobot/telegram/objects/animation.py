from .base import BaseObject
from .photosize import PhotoSize
from typing import Optional

class Animation (BaseObject):
    """This object represents an animation file (GIF or H.264/MPEG-4 AVC video without sound).

    Args:
        file_id (str) : Identifier for this file, which can be used to download or reuse the file

        file_unique_id (str) : Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.

        width (int) : Video width as defined by sender

        height (int) : Video height as defined by sender

        duration (int) : Duration of the video in seconds as defined by sender

        thumb (obj) : Optional. Animation thumbnail as defined by sender

        file_name (str) : Optional. Original animation filename as defined by sender

        mime_type (str) : Optional. MIME type of the file as defined by sender

        file_size (int) :   Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. 
                            But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value.
    """

    __slots__ = (
        "file_id",
        "file_unique_id",
        "width",
        "height",
        "duration",
        "thumb",
        "file_name",
        "mime_type",
        "file_size"
    )

    def __init__(self, 
                 file_id:str, 
                 file_unique_id:str, 
                 width:int, height:int, 
                 duration:int
                ) -> None:
        
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.duration = duration
        self.thumb: Optional[PhotoSize] = None
        self.file_name: Optional[str] = None
        self.mime_type: Optional[str] = None
        self.file_size: Optional[int] = None
