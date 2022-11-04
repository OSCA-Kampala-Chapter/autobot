from .base import BaseObject
from . import PhotoSize
from typing import Optional

class Document(BaseObject):
    """This object represents a general file (as opposed to photos, voice messages and audio files).

    Args:
        file_id (str) : Identifier for this file, which can be used to download or reuse the file

        file_unique_id (str) : Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.

        thumb (obj) : Optional. Document thumbnail as defined by sender

        file_name (str) : Optional. Original filename as defined by sender

        mime_type (str) : Optional. MIME type of the file as defined by sender

        file_size (int) :   Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. 
                            But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value.
    """

    __slots__ = (
        "thumb",
        "file_name",
        "mime_type",
        "file_size"
    )

    def __init__(self, file_id:str, file_unique_id:str) -> None:
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.thumb: Optional[PhotoSize] = None
        self.file_name: Optional[str] = None
        self.mime_type: Optional[str] = None
        self.file_size: Optional[int] = None
