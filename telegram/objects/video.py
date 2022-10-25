class Video:
    def __init__(self,
        file_id,
        file_unique_id,
        width,
        height,
        duration,
        thumb = None,
        file_name = None,
        mime_type = None,
        file_size = None
        ):

        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.duration = duration
        self.thumb = thumb
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size
    
class VideoChatEnded:
    def __init__(self, duration):
        self.duration = duration
    
class VideoChatParticipantsInvited:
    def __init__(self, users):
        self.users = users

    
class VideoChatScheduled:
    def __init__(self, start_date):
        self.start_date = start_date

    
class VideoChatStarted:
    #This object represents a service message about a video chat started in the chat. 
    #
    #Currently holds no information.
    pass

    
class VideoNote:
    def __init__(self,
        file_id,
        file_unique_id,
        length,
        duration,
        thumb = None,
        file_size = None
        ):

        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.length = length
        self.duration = duration
        self.thumb = thumb
        self.file_size = file_size