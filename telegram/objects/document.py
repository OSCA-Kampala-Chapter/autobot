from .base import BaseObject

class Document(BaseObject):
    def __init__(self,
        file_id,
        file_unique_id,
        thumb = None,
        file_name = None,
        mime_type = None,
        file_size = None
        ):

        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.thumb = thumb
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size
