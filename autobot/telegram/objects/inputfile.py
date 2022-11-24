from autobot.telegram.objects.base import BaseObject
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from autobot.telegram.objects.message import MessageEntity

class InputFile(BaseObject):
    """
    This object represents the contents of a file to be uploaded.
    Must be posted using multipart/form-data in the usual way that files are uploaded via the browser.
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
    
    
    def __init__(self, type: str = None, media: str = None) -> None:
        self.type = type
        self.media = media
        self.thumb: Optional[InputFile] = None
        self.caption: Optional[str] = None 
        self.parse_mode: Optional[str] = None
        self.caption_entities: Optional[list[MessageEntity]] = None
        self.width: Optional[int] = None
        self.height: Optional[int] = None 
        self.duration: Optional[int] = None
    
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


    def __init__(self, type: str = None, media: str = None) -> None:
        self.type = type
        self.media = media
        self.thumb: Optional[InputFile] = None
        self.caption: Optional[str] = None 
        self.parse_mode: Optional[str] = None
        self.caption_entities: Optional[list[MessageEntity]] = None
        self.width: Optional[int] = None
        self.height: Optional[int] = None 
        self.duration: Optional[int] = None
    
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


    def __init__(self, type: str = None, media: str = None) -> None:
        self.type = type
        self.media = media
        self.thumb: Optional[InputFile] = None
        self.caption: Optional[str] = None 
        self.parse_mode: Optional[str] = None
        self.caption_entities: Optional[list[MessageEntity]] = None
        self.duration: Optional[int] = None
        self.performer: Optional[str] = None
        self.title: Optional[str] = None
    
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


    def __init__(self, type: str = None, media: str = None) -> None:
        self.type = type
        self.media = media
        self.thumb: Optional[InputFile] = None
        self.caption: Optional[str] = None 
        self.parse_mode: Optional[str] = None
        self.caption_entities: Optional[list[MessageEntity]] = None
        self.disable_content_type_detection: Optional[bool] = None
    
class InputMediaPhoto(BaseObject):
    """Represents a photo to be sent.
        Args:
            type (str): Type of the result, must be photo
            media (str): File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name.
            caption (str): Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing
            parse_mode 	(str): Optional. Mode for parsing entities in the photo caption
            caption_entities (list): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    """


    def __init__(self, type: str = None, media: str = None) -> None:
        self.type = type
        self.media = media
        self.caption: Optional[str] = None 
        self.parse_mode: Optional[str] = None
        self.caption_entities: Optional[list[MessageEntity]] = None
    
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
    

    def __init__(self, type: str = None, media: str = None) -> None:
        self.type = type
        self.media = media
        self.thumb: Optional[InputFile] = None
        self.caption: Optional[str] = None 
        self.parse_mode: Optional[str] = None
        self.caption_entities: Optional[list[MessageEntity]] = None
        self.width: Optional[int] = None
        self.height: Optional[int] = None
        self.duration: Optional[int] = None
        self.support_streaming: Optional[bool] = None
    