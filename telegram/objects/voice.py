from .base import BaseObject

class Voice(BaseObject):
    def __init__ (self,
        file_id,
        file_unique_id,
        duration,
        mime_type = None,
        file_size = None,
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.duration = duration
        self.mime_type = mime_type
        self.file_size = file_size