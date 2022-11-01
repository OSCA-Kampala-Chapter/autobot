from .base import BaseObject

class InputFile(BaseObject):
    """This object represents the contents of a file to be uploaded.
    
    """
    
class InputMedia(BaseObject):
    """
    This object represents the content of a media message to be sent.

    Args:
        type (str): Type of the result, must be photo
        media (str): File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name.
        caption (str): Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing
        parse_mode (str): Optional. Mode for parsing entities in the photo caption. See formatting options for more details.
        caption_entities (List[:obj:`MessageEntity`]): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    """
    
    __slots__ = (
        'type',
        'media',
        'caption', 
        'parse_mode', 
        'caption_entities',
    )
    
    def __init__(self, type, media):
        self.type = type
        self.media = media
        self.caption = None
        self.parse_mode = None
        self.caption_entities = None
    
class InputMediaAnimation(BaseObject):
    """Represents an animation file (GIF or H.264/MPEG-4 AVC video without sound) to be sent.

        Args:
            type (str_): Type of the result, must be animation.

            media (str): File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name.

            thumb (str): Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>

            caption (str): Optional. Caption of the animation to be sent, 0-1024 characters after entities parsing

            parse_mode (str): Optional. Mode for parsing entities in the animation caption.

            caption_entities (list): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode

            width (int): Optional. Animation width

            height (int): Optional. Animation height 

            duration (int): Optional . Animation duration in seconds 
    """

    __slots__ = (
        "type",
        "media",
        "thumb",
        "caption",
        "parse_mode",
        "caption_entities",
        "width",
        "height",
        "duration"
    )   

    def __init__(self, type, media):
        self.type = type
        self.media = media
        self.thumb = None
        self.caption = None 
        self.parse_mode = None 
        self.caption_entities = None
        self.width = None 
        self.height = None 
        self.duration = None 
    
class InputMediaAudio(BaseObject):
    """Represents an audio file to be treated as music to be sent.

        Args:
            type (str_): Type of the result, must be audio.

            media (str): File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name.

            thumb (str): Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>

            caption (str): Optional. Caption of the audio to be sent, 0-1024 characters after entities parsing

            parse_mode (str): Optional. Mode for parsing entities in the audio caption

            caption_entities (list): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode

            duration (int): Optional. Duration of the audio in seconds

            performer (str): Optional. Performer of the audio

            title (str): Optional. Title of the audio
    """

    __slots__ = (
        "type",
        "media",
        "thumb",
        "caption",
        "parse_mode",
        "caption_entities",
        "duration",
        "performer",
        "title"
    )   

    def __init__(self, type, media):
        self.type = type
        self.media = media
        self.thumb = None
        self.caption = None 
        self.parse_mode = None 
        self.caption_entities = None
        self.duration = None 
        self.title = None
        self.performer = None 
    
class InputMediaDocument(BaseObject):
    """Represents a general file to be sent.

    Args:
        type (str): Type of the result, must be document.

        media (str): File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name

        thumb (str): Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>.

        caption (str): Optional. Caption of the document to be sent, 0-1024 characters after entities parsing

        parse_mode (str): Optional. Mode for parsing entities in the document caption.

        caption_entities (list): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode

        disable_content_type_detection (boolean): Optional. Disables automatic server-side content type detection for files uploaded using multipart/form-data. Always True, if the document is sent as part of an album.
    """

    __slots__ = (
        "type",
        "media",
        "thumb",
        "caption",
        "parse_mode",
        "caption_entities",
        "disable_content_type_detection"
    )

    def __init__(self, type, media):
        self.type = type
        self.media = media
        self.thumb = None 
        self.caption = None 
        self.parse_mode = None 
        self.caption_entities = None 
        self.disable_content_type_detection = None
    
class InputMediaPhoto(BaseObject):
    """Represents a photo to be sent.

        Args:
            type (str): Type of the result, must be photo

            media (str): File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name.

            caption (str): Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing

            parse_mode 	(str): Optional. Mode for parsing entities in the photo caption

            caption_entities (list): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    """

    __slots__ = (
        "type",
        "media",
        "caption",
        "parse_mode",
        "caption_entities"
    )

    def __init__(self, type, media):
        self.type = type
        self.media = media
        self.caption = None 
        self.parse_mode = None
        self.caption_entities = None
    
class InputMediaVideo(BaseObject):
    """Represents a video to be sent.

        Args:
            type (str_): Type of the result, must be video.

            media (str): File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name.

            thumb (str): Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>

            caption (str): Optional. Caption of the video to be sent, 0-1024 characters after entities parsing

            parse_mode (str): Optional. Mode for parsing entities in the video caption.

            caption_entities (list): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode

            width (int): Optional. Video width

            height (int): Optional. Video height 

            duration (int): Optional . Video duration in seconds

            supporting_streaming (bool): Optional. Pass True if the uploaded video is suitable for streaming  
    """
    
    __slots__ = (
        "type",
        "media",
        "thumb",
        "caption",
        "parse_mode",
        "caption_entities",
        "width",
        "height",
        "duration",
        "support_streaming"
    )

    def __init__(self, type, media):
        self.type = type
        self.media = media
        self.thumb = None
        self.caption = None 
        self.parse_mode = None 
        self.caption_entities = None
        self.width = None 
        self.height = None 
        self.duration = None 
        self.support_streaming = None 
    
