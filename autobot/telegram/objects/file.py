from .base import BaseObject

class File(BaseObject):
    def __init__(self,
        file_id,
        file_unique_id,
        file_size = None,
        file_path = None
        ):

        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.file_size = file_size
        self.file_path = file_path
      
