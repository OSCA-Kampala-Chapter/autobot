class Audio:
    def __init__(self, 
        file_id,
        file_unique_id,
        duration = None,
        performer = None,
        title = None,
        file_name = None,
        mime_type = None,
        file_size = None,
        thumb = None
        ):

        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.duration = duration
        self.performer = performer
        self.title = title
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size
        self.thumb = thumb
