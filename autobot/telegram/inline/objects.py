from ..objects import BaseObject
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects import User, Location, MessageEntity, InlineKeyboardMarkup


class InputMessageContent(BaseObject):
    """
    This object represents the content of a message to be sent as a result of an inline query. 
    Telegram clients currently support the following 5 types:
    
    `InputTextMessageContent`

    `InputLocationMessageContent`

    `InputVenueMessageContent`

    `InputContactMessageContent`
    
    `InputInvoiceMessageContent`
    """
    pass

class InlineQuery(BaseObject):
    
    __slots__ = ("id",
                "from_",
                "query",
                "offset",
                "chat_type",
                "location",
                )
    def __init__(self, id: str, from_: User, query: str, offset: str) -> None:
        self.id = id
        self.from_ = from_
        self.query = query
        self.offset = offset
        self.chat_type: Optional[str] = None
        self.location: Optional[Location] = None
        
class InlineQueryResult (BaseObject):
    """
    Base class for InlineQueryResult* objects.
    """
    __slots__ = ("type",
                "id",
                )
    def __init__ (self, type: str, id: str) -> None:
        self.type = type
        self.id = id
        
class InlineQueryResultCachedAudio (InlineQueryResult):
    """
    Represents a link to an MP3 audio file stored on the Telegram servers. 
    By default, this audio file will be sent by the user. 
    Alternatively, you can use `input_message_content` to send a message 
    with the specified content instead of the audio.

    Args:
        type (:obj:`str`): Type of the result, must be audio.

        id (:obj:`str`): Unique identifier for this result, 1-64 bytes.

        audio_file_id (:obj:`str`): A valid file identifier for the audio file.

        caption (:obj:`str`, optional): Caption, 0-1024 characters after entities parsing.

        parse_mode (:obj:`str`, optional): Mode for parsing entities in the audio caption. 
        See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.

        caption_entities (:obj:`list` of :obj:`MessageEntity`, optional): List of special entities that 
        appear in the caption, which can be specified instead of parse_mode.

        input_message_content (:obj:`InputMessageContent`, optional): Content of the message to be sent instead of the audio.

        reply_markup (:obj:`InlineKeyboardMarkup`, optional): Inline keyboard attached to the message.
    """
    __slots__ = ("type",
                "id",
                "audio_file_id",
                "caption",
                "parse_mode",
                "caption_entities",
                "input_message_content",
                "reply_markup",
                )
    def __init__ (self, id: str, audio_file_id: str, type: str = "audio") -> None:
        self.id = id
        self.audio_file_id = audio_file_id
        self.caption: Optional[str] = None
        self.parse_mode: Optional[str] = None
        self.caption_entities: Optional[list] = None
        self.input_message_content: Optional[InputMessageContent] = None
        self.reply_markup: Optional[InlineKeyboardMarkup] = None


class InlineQueryResultCachedDocument (InlineQueryResult):
    """
    Represents a link to a file stored on the Telegram servers. 
    By default, this file will be sent by the user with an optional caption. 
    Alternatively, you can use `input_message_content` to send a message with the specified content instead of the file.

    Args:
        type (:obj:`str`): Type of the result, must be document.

        id (:obj:`str`): Unique identifier for this result, 1-64 bytes.

        title (:obj:`str`): Title for the result.

        document_file_id (:obj:`str`): A valid file identifier for the file.

        description (:obj:`str`, optional): Short description of the result.

        caption (:obj:`str`, optional): Caption, 0-1024 characters after entities parsing.

        parse_mode (:obj:`str`, optional): Mode for parsing entities in the document caption. 
        See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.

        caption_entities (:obj:`list` of :obj:`MessageEntity`, optional): List of special entities that 
        appear in the caption, which can be specified instead of parse_mode.

        input_message_content (:obj:`InputMessageContent`, optional): Content of the message to be sent instead of the file.

        reply_markup (:obj:`InlineKeyboardMarkup`, optional): Inline keyboard attached to the message.
    """
    __slots__ = ("type",
                "id",
                "title",
                "document_file_id",
                "description",
                "caption",
                "parse_mode",
                "caption_entities",
                "input_message_content",
                "reply_markup",
                )
    def __init__ (self, id: str, title: str, document_file_id: str, type: str = "document") -> None:
        self.id = id
        self.title = title
        self.type = type
        self.document_file_id = document_file_id
        self.description: Optional[str] = None
        self.caption: Optional[str] = None
        self.parse_mode: Optional[str] = None
        self.caption_entities: Optional[list] = None
        self.input_message_content: Optional[InputMessageContent] = None
        self.reply_markup: Optional[InlineKeyboardMarkup] = None


class InlineQueryResultCachedGif (InlineQueryResult):
    """
    Represents a link to an animated GIF file stored on the Telegram servers. 
    By default, this animated GIF file will be sent by the user with an optional caption. 
    Alternatively, you can use `input_message_content` to send a message with specified content instead of the animation.

    Args:
        type (:obj:`str`): Type of the result, must be gif.

        id (:obj:`str`): Unique identifier for this result, 1-64 bytes.

        gif_file_id (:obj:`str`): A valid file identifier for the GIF file.

        title (:obj:`str`, optional): Title for the result.

        caption (:obj:`str`, optional): Caption, 0-1024 characters after entities parsing.

        parse_mode (:obj:`str`, optional): Mode for parsing entities in the animation caption. 
        See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.

        caption_entities (:obj:`list` of :obj:`MessageEntity`, optional): List of special entities that 
        appear in the caption, which can be specified instead of parse_mode.

        input_message_content (:obj:`InputMessageContent`, optional): Content of the message to be sent instead of the GIF animation.

        reply_markup (:obj:`InlineKeyboardMarkup`, optional): Inline keyboard attached to the message.
    """
    __slots__ = ("type",
                "id",
                "gif_file_id",
                "title",
                "caption",
                "parse_mode",
                "caption_entities",
                "input_message_content",
                "reply_markup",
                )
    def __init__ (self, id: str, gif_file_id: str, type: str = "gif") -> None:
        self.id = id
        self.type = type
        self.gif_file_id = gif_file_id
        self.title: Optional[str] = None
        self.caption: Optional[str] = None
        self.parse_mode: Optional[str] = None
        self.caption_entities: Optional[list] = None
        self.input_message_content: Optional[InputMessageContent] = None
        self.reply_markup: Optional[InlineKeyboardMarkup] = None


class InlineQueryResultCachedMpeg4Gif (InlineQueryResult):
    """
    Represents a link to a video animation (H.264/MPEG-4 AVC video without sound) stored on the Telegram servers. 
    By default, this animated MPEG-4 file will be sent by the user with an optional caption. 
    Alternatively, you can use `input_message_content` to send a message with the specified content instead of the animation.

    Args:
        type (:obj:`str`): Type of the result, must be mpeg4_gif.

        id (:obj:`str`): Unique identifier for this result, 1-64 bytes.

        mpeg4_file_id (:obj:`str`): A valid file identifier for the MP4 file.

        title (:obj:`str`, optional): Title for the result.

        caption (:obj:`str`, optional): Caption, 0-1024 characters after entities parsing.

        parse_mode (:obj:`str`, optional): Mode for parsing entities in the animation caption. 
        See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.

        caption_entities (:obj:`list` of :obj:`MessageEntity`, optional): List of special entities that 
        appear in the caption, which can be specified instead of parse_mode.

        input_message_content (:obj:`InputMessageContent`, optional): Content of the message to be sent instead of the video animation.

        reply_markup (:obj:`InlineKeyboardMarkup`, optional): Inline keyboard attached to the message.
    """
    __slots__ = ("type",
                "id",
                "mpeg4_file_id",
                "title",
                "caption",
                "parse_mode",
                "caption_entities",
                "input_message_content",
                "reply_markup",
                )
    def __init__ (self, id: str, mpeg4_file_id: str, type: str = "mpeg4_gif") -> None:
        self.id = id
        self.type = type
        self.mpeg4_file_id = mpeg4_file_id
        self.title: Optional[str] = None
        self.caption: Optional[str] = None
        self.parse_mode: Optional[str] = None
        self.caption_entities: Optional[list] = None
        self.input_message_content: Optional[InputMessageContent] = None
        self.reply_markup: Optional[InlineKeyboardMarkup] = None


class InlineQueryResultCachedSticker (InlineQueryResult):
    """
    Represents a link to a sticker stored on the Telegram servers. 
    By default, this sticker will be sent by the user. 
    Alternatively, you can use `input_message_content` to send a message with the specified content instead of the sticker.

    Args:
        type (:obj:`str`): Type of the result, must be sticker.

        id (:obj:`str`): Unique identifier for this result, 1-64 bytes.

        sticker_file_id (:obj:`str`): A valid file identifier of the sticker.

        input_message_content (:obj:`InputMessageContent`, optional): Content of the message to be sent instead of the sticker.

        reply_markup (:obj:`InlineKeyboardMarkup`, optional): Inline keyboard attached to the message.
    """
    __slots__ = ("type",
                "id",
                "sticker_file_id",
                "input_message_content",
                "reply_markup",
                )
    def __init__ (self, id: str, sticker_file_id: str, type: str = "sticker") -> None:
        self.id = id
        self.type = type
        self.sticker_file_id = sticker_file_id
        self.input_message_content: Optional[InputMessageContent] = None
        self.reply_markup: Optional[InlineKeyboardMarkup] = None



class InlineQueryResultCachedPhoto(InlineQueryResult):
    """
    Represents a link to a photo stored on the Telegram servers. 
    By default, this photo will be sent by the user with an optional 
    caption. Alternatively, you can use `input_message_content` to send 
    a message with the specified content instead of the photo.

    Args:
        type (:obj:`str`): Type of the result, must be photo.

        id (:obj:`str`): Unique identifier for this result, 1-64 bytes.

        photo_file_id (:obj:`str`): A valid file identifier of the photo.

        title (:obj:`str`, optional): Title for the result.

        description (:obj:`str`, optional): Short description of the result.

        caption (:obj:`str`, optional): Caption of the photo to be sent, 0-1024 characters after entities parsing.

        parse_mode (:obj:`str`, optional): Mode for parsing entities in the photo caption. 
        See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.

        caption_entities (:obj:`list` of :obj:`MessageEntity`, optional): List of special entities that 
        appear in the caption, which can be specified instead of parse_mode.

        input_message_content (:obj:`InputMessageContent`, optional): Content of the message to be sent instead of the photo.

        reply_markup (:obj:`InlineKeyboardMarkup`, optional): Inline keyboard attached to the message.
    """
    __slots__ = ("type",
                "id",
                "photo_file_id",
                "title",
                "description",
                "caption",
                "parse_mode",
                "caption_entities",
                "input_message_content",
                "reply_markup",
                )
    def __init__ (self, id: str, photo_file_id: str, type: str = "photo") -> None:
        self.id = id
        self.type = type
        self.photo_file_id = photo_file_id
        self.title: Optional[str] = None
        self.description: Optional[str] = None
        self.caption: Optional[str] = None
        self.parse_mode: Optional[str] = None
        self.caption_entities: Optional[list] = None
        self.input_message_content: Optional[InputMessageContent] = None
        self.reply_markup: Optional[InlineKeyboardMarkup] = None
        

class InlineQueryResultCachedVideo(InlineQueryResult):
    """
    Represents a link to a video file stored on the Telegram servers. 
    By default, this video file will be sent by the user with an optional 
    caption. Alternatively, you can use `input_message_content` to send 
    a message with the specified content instead of the video.

    Args:
        type (:obj:`str`): Type of the result, must be video.

        id (:obj:`str`): Unique identifier for this result, 1-64 bytes.

        video_file_id (:obj:`str`): A valid file identifier for the video file.

        title (:obj:`str`, optional): Title for the result.

        description (:obj:`str`, optional): Short description of the result.

        caption (:obj:`str`, optional): Caption of the video to be sent, 0-1024 characters after entities parsing.

        parse_mode (:obj:`str`, optional): Mode for parsing entities in the video caption. 
        See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.

        caption_entities (:obj:`list` of :obj:`MessageEntity`, optional): List of special entities that 
        appear in the caption, which can be specified instead of parse_mode.

        input_message_content (:obj:`InputMessageContent`, optional): Content of the message to be sent instead of the video.

        reply_markup (:obj:`InlineKeyboardMarkup`, optional): Inline keyboard attached to the message.
    """
    __slots__ = ("type",
                "id",
                "video_file_id",
                "title",
                "description",
                "caption",
                "parse_mode",
                "caption_entities",
                "input_message_content",
                "reply_markup",
                )
    def __init__ (self, id: str, video_file_id: str, type: str = "video") -> None:
        self.id = id
        self.type = type
        self.video_file_id = video_file_id
        self.title: Optional[str] = None
        self.description: Optional[str] = None
        self.caption: Optional[str] = None
        self.parse_mode: Optional[str] = None
        self.caption_entities: Optional[list] = None
        self.input_message_content: Optional[InputMessageContent] = None
        self.reply_markup: Optional[InlineKeyboardMarkup] = None


class InlineQueryResultCachedVoice(InlineQueryResult):
    """
    Represents a link to a voice message stored on the Telegram servers. 
    By default, this voice message will be sent by the user. Alternatively, 
    you can use `input_message_content` to send a message with the specified 
    content instead of the voice message.

    Args:
        type (:obj:`str`): Type of the result, must be voice.

        id (:obj:`str`): Unique identifier for this result, 1-64 bytes.

        voice_file_id (:obj:`str`): A valid file identifier for the voice message.

        title (:obj:`str`): Voice message title.

        caption (:obj:`str`, optional): Caption, 0-1024 characters after entities parsing.

        parse_mode (:obj:`str`, optional): Mode for parsing entities in the voice message caption. 
        See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.

        caption_entities (:obj:`list` of :obj:`MessageEntity`, optional): List of special entities that 
        appear in the caption, which can be specified instead of parse_mode.

        input_message_content (:obj:`InputMessageContent`, optional): Content of the message to be sent instead of the voice message.

        reply_markup (:obj:`InlineKeyboardMarkup`, optional): Inline keyboard attached to the message.
    """
    __slots__ = ("type",
                "id",
                "voice_file_id",
                "title",
                "caption",
                "parse_mode",
                "caption_entities",
                "input_message_content",
                "reply_markup",
                )
    def __init__ (self, id: str, voice_file_id: str, title: str, type: str = "voice") -> None:
        self.id = id
        self.type = type
        self.voice_file_id = voice_file_id
        self.title = title
        self.caption: Optional[str] = None
        self.parse_mode: Optional[str] = None
        self.caption_entities: Optional[list[MessageEntity]] = None
        self.input_message_content: Optional[InputMessageContent] = None
        self.reply_markup: Optional[InlineKeyboardMarkup] = None


class InlineQueryResultArticle(InlineQueryResult):
    """
    Represents a link to an article or web page.

    Args:
        type (:obj:`str`): Type of the result, must be article.

        id (:obj:`str`): Unique identifier for this result, 1-64 Bytes.

        title (:obj:`str`): Title of the result.

        input_message_content (:obj:`InputMessageContent`): Content of the message to be sent.

        reply_markup (:obj:`InlineKeyboardMarkup`, optional): Inline keyboard attached to the message.

        url (:obj:`str`, optional): URL of the result.

        hide_url (:obj:`bool`, optional): Pass True, if you don't want the URL to be shown in the message.

        description (:obj:`str`, optional): Short description of the result.

        thumb_url (:obj:`str`, optional): Url of the thumbnail for the result.

        thumb_width (:obj:`int`, optional): Thumbnail width.

        thumb_height (:obj:`int`, optional): Thumbnail height.
    """
    __slots__ = ("type",
                "id",
                "title",
                "input_message_content",
                "reply_markup",
                "url",
                "hide_url",
                "description",
                "thumb_url",
                "thumb_width",
                "thumb_height",
                )
    def __init__ (self, id: str, title: str, input_message_content: InputMessageContent, type: str = "article") -> None:
        self.id = id
        self.type = type
        self.title = title
        self.input_message_content = input_message_content
        self.reply_markup: Optional[InlineKeyboardMarkup] = None
        self.url: Optional[str] = None
        self.hide_url: Optional[bool] = None
        self.description: Optional[str] = None
        self.thumb_url: Optional[str] = None
        self.thumb_width: Optional[int] = None
        self.thumb_height: Optional[int] = None


class InlineQueryResultPhoto(InlineQueryResult):
    """
    Represents a link to a photo. By default, this photo will be sent by the user with optional caption. 
    Alternatively, you can use `input_message_content` to send a message with the specified content instead of the photo.

    Args:
        type (:obj:`str`): Type of the result, must be photo.

        id (:obj:`str`): Unique identifier for this result, 1-64 bytes.

        photo_url (:obj:`str`): A valid URL of the photo. Photo must be in jpeg format. 
        Photo size must not exceed 5MB.

        thumb_url (:obj:`str`): URL of the thumbnail for the photo.

        photo_width (:obj:`int`, optional): Width of the photo.

        photo_height (:obj:`int`, optional): Height of the photo.

        title (:obj:`str`, optional): Title for the result.

        description (:obj:`str`, optional): Short description of the result.

        caption (:obj:`str`, optional): Caption of the photo to be sent, 0-1024 characters after entities parsing.

        parse_mode (:obj:`str`, optional): Mode for parsing entities in the photo caption. 
        See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.

        caption_entities (:obj:`list` of :obj:`MessageEntity`, optional): List of special entities that 
        appear in the caption, which can be specified instead of parse_mode.

        input_message_content (:obj:`InputMessageContent`, optional): Content of the message to be sent instead of the photo.

        reply_markup (:obj:`InlineKeyboardMarkup`, optional): Inline keyboard attached to the message.
    """
    __slots__ = ("type",
                "id",
                "photo_url",
                "thumb_url",
                "photo_width",
                "photo_height",
                "title",
                "description",
                "caption",
                "parse_mode",
                "caption_entities",
                "input_message_content",
                "reply_markup",
                )
    def __init__ (self, id: str, photo_url: str, thumb_url: str, type: str = "photo") -> None:
        self.id = id
        self.type = type
        self.photo_url = photo_url
        self.thumb_url = thumb_url
        self.photo_width: Optional[int] = None
        self.photo_height: Optional[int] = None
        self.title: Optional[str] = None
        self.description: Optional[str] = None
        self.caption: Optional[str] = None
        self.parse_mode: Optional[str] = None
        self.caption_entities: Optional[list[MessageEntity]] = None
        self.input_message_content: Optional[InputMessageContent] = None
        self.reply_markup: Optional[InlineKeyboardMarkup] = None


class InlineQueryResultGif(InlineQueryResult):
    """
    Represents a link to an animated GIF file. 
    By default, this animated GIF file will be sent by the user 
    with optional caption. Alternatively, you can 
    use `input_message_content` to send a message with 
    the specified content instead of the animation.

    Args:
        type (:obj:`str`): Type of the result, must be gif.

        id (:obj:`str`): Unique identifier for this result, 1-64 bytes.

        gif_url (:obj:`str`): A valid URL for the GIF file. 
        File size must not exceed 1MB.

        gif_width (:obj:`int`, optional): Width of the GIF.

        gif_height (:obj:`int`, optional): Height of the GIF.

        gif_duration (:obj:`int`, optional): Duration of the GIF.

        thumb_url (:obj:`str`): URL of the static thumbnail for the result (jpeg or gif).

        thumb_mime_type (:obj:`str`, optional): MIME type of the thumbnail, must be one of “image/jpeg”, “image/gif”, or “video/mp4”. 
        Defaults to “image/jpeg”.

        title (:obj:`str`, optional): Title for the result.

        caption (:obj:`str`, optional): Caption of the GIF file to be sent, 0-1024 characters after entities parsing.

        parse_mode (:obj:`str`, optional): Mode for parsing entities in the GIF caption. 
        See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.

        caption_entities (:obj:`list` of :obj:`MessageEntity`, optional): List of special entities that 
        appear in the caption, which can be specified instead of parse_mode.

        input_message_content (:obj:`InputMessageContent`, optional): Content of the message to be sent instead of the GIF animation.

        reply_markup (:obj:`InlineKeyboardMarkup`, optional): Inline keyboard attached to the message.
    """
    __slots__ = ("type",
                "id",
                "gif_url",
                "gif_width",
                "gif_height",
                "gif_duration",
                "thumb_url",
                "thumb_mime_type",
                "title",
                "caption",
                "parse_mode",
                "caption_entities",
                "input_message_content",
                "reply_markup",
                )
    def __init__ (self, id: str, gif_url: str, thumb_url: str, type: str = "gif") -> None:
        self.id = id
        self.type = type
        self.gif_url = gif_url
        self.gif_width: Optional[int] = None
        self.gif_height: Optional[int] = None
        self.gif_duration: Optional[int] = None
        self.thumb_url = thumb_url
        self.thumb_mime_type: Optional[str] = None
        self.title: Optional[str] = None
        self.caption: Optional[str] = None
        self.parse_mode: Optional[str] = None
        self.caption_entities: Optional[list[MessageEntity]] = None
        self.input_message_content: Optional[InputMessageContent] = None
        self.reply_markup: Optional[InlineKeyboardMarkup] = None


class InlineQueryResultMpeg4Gif(InlineQueryResult):
    """
    Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). 
    By default, this animated MPEG-4 file will be sent by the user with optional caption. 
    Alternatively, you can use `input_message_content` to send a message with the specified content instead of the animation.

    Args:
        type (:obj:`str`): Type of the result, must be mpeg4_gif.

        id (:obj:`str`): Unique identifier for this result, 1-64 bytes.

        mpeg4_url (:obj:`str`): A valid URL for the MP4 file. 
        File size must not exceed 1MB.

        mpeg4_width (:obj:`int`, optional): Video width.

        mpeg4_height (:obj:`int`, optional): Video height.

        mpeg4_duration (:obj:`int`, optional): Video duration.

        thumb_url (:obj:`str`): URL of the static thumbnail (jpeg or gif) for the result.

        thumb_mime_type (:obj:`str`, optional): MIME type of the thumbnail, must be one of “image/jpeg”, “image/gif”, or “video/mp4”. 
        Defaults to “image/jpeg”.

        title (:obj:`str`, optional): Title for the result.

        caption (:obj:`str`, optional): Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing.

        parse_mode (:obj:`str`, optional): Mode for parsing entities in the MPEG-4 file caption. 
        See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.

        caption_entities (:obj:`list` of :obj:`MessageEntity`, optional): List of special entities that 
        appear in the caption, which can be specified instead of parse_mode.

        input_message_content (:obj:`InputMessageContent`, optional): Content of the message to be sent instead of the video animation.

        reply_markup (:obj:`InlineKeyboardMarkup`, optional): Inline keyboard attached to the message.
    """
    __slots__ = ("type",
                "id",
                "mpeg4_url",
                "mpeg4_width",
                "mpeg4_height",
                "mpeg4_duration",
                "thumb_url",
                "thumb_mime_type",
                "title",
                "caption",
                "parse_mode",
                "caption_entities",
                "input_message_content",
                "reply_markup",
                )

    def __init__ (self, id: str, mpeg4_url: str, thumb_url: str, type: str = "mpeg4_gif") -> None:
        self.id = id
        self.type = type
        self.mpeg4_url = mpeg4_url
        self.mpeg4_width: Optional[int] = None
        self.mpeg4_height: Optional[int] = None
        self.mpeg4_duration: Optional[int] = None
        self.thumb_url = thumb_url
        self.thumb_mime_type: Optional[str] = None
        self.title: Optional[str] = None
        self.caption: Optional[str] = None
        self.parse_mode: Optional[str] = None
        self.caption_entities: Optional[list[MessageEntity]] = None
        self.input_message_content: Optional[InputMessageContent] = None
        self.reply_markup: Optional[InlineKeyboardMarkup] = None


class InlineQueryResultVideo(InlineQueryResult):
    """
    Represents a link to a page containing an embedded video player or a video file. 
    By default, this video file will be sent by the user with an optional caption. 
    Alternatively, you can use `input_message_content` to send a message with the specified content instead of the video.

    `Note`: If an InlineQueryResultVideo message contains an embedded video (e.g., YouTube), 
    you must replace its content using `input_message_content`.

    Args:
        type (:obj:`str`): Type of the result, must be video.

        id (:obj:`str`): Unique identifier for this result, 1-64 bytes.

        video_url (:obj:`str`): A valid URL for the embedded video player or video file.

        mime_type (:obj:`str`): Mime type of the content of video url, “text/html” or “video/mp4”.

        thumb_url (:obj:`str`): URL of the thumbnail (jpeg only) for the video.

        title (:obj:`str`): Title for the result.

        caption (:obj:`str`, optional): Caption of the video to be sent, 0-1024 characters after entities parsing.

        parse_mode (:obj:`str`, optional): Mode for parsing entities in the video caption. 
        See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.

        caption_entities (:obj:`list` of :obj:`MessageEntity`, optional): List of special entities that 
        appear in the caption, which can be specified instead of parse_mode.

        video_width (:obj:`int`, optional): Video width.

        video_height (:obj:`int`, optional): Video height.

        video_duration (:obj:`int`, optional): Video duration in seconds.

        description (:obj:`str`, optional): Short description of the result.

        input_message_content (:obj:`InputMessageContent`, optional): Content of the message to be sent instead of the video. 
        This field is required if InlineQueryResultVideo is used to send an HTML-page as a result (e.g., a YouTube video).

        reply_markup (:obj:`InlineKeyboardMarkup`, optional): Inline keyboard attached to the message.
    """
    __slots__ = ("type",
                "id",
                "video_url",
                "mime_type",
                "thumb_url",
                "title",
                "caption",
                "parse_mode",
                "caption_entities",
                "video_width",
                "video_height",
                "video_duration",
                "description",
                "input_message_content",
                "reply_markup",
                )

    def __init__ (self, id: str, video_url: str, mime_type: str, thumb_url: str, title: str, type: str = "video") -> None:
        self.id = id
        self.type = type
        self.video_url = video_url
        self.mime_type = mime_type
        self.thumb_url = thumb_url
        self.title = title
        self.caption: Optional[str] = None
        self.parse_mode: Optional[str] = None
        self.caption_entities: Optional[list[MessageEntity]] = None
        self.video_width: Optional[int] = None
        self.video_height: Optional[int] = None
        self.video_duration: Optional[int] = None
        self.description: Optional[str] = None
        self.input_message_content: Optional[InputMessageContent] = None
        self.reply_markup: Optional[InlineKeyboardMarkup] = None


class InlineQueryResultAudio(InlineQueryResult):
    """
    Represents a link to an mp3 audio file. By default, this audio file will be sent by the user. 
    Alternatively, you can use `input_message_content` to send a message with the specified content instead of the audio.

    Args:
        type (:obj:`str`): Type of the result, must be audio.

        id (:obj:`str`): Unique identifier for this result, 1-64 bytes.

        audio_url (:obj:`str`): A valid URL for the audio file.

        title (:obj:`str`): Title.

        caption (:obj:`str`, optional): Caption, 0-1024 characters after entities parsing.

        parse_mode (:obj:`str`, optional): Mode for parsing entities in the audio caption. 
        See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.

        caption_entities (:obj:`list` of :obj:`MessageEntity`, optional): List of special entities that 
        appear in the caption, which can be specified instead of parse_mode.

        performer (:obj:`str`, optional): Performer.

        audio_duration (:obj:`int`, optional): Audio duration in seconds.

        input_message_content (:obj:`InputMessageContent`, optional): Content of the message to be sent instead of the audio.

        reply_markup (:obj:`InlineKeyboardMarkup`, optional): Inline keyboard attached to the message.
    """
    __slots__ = ("type",
                "id",
                "audio_url",
                "title",
                "caption",
                "parse_mode",
                "caption_entities",
                "performer",
                "audio_duration",
                "input_message_content",
                "reply_markup",
                )

    def __init__ (self, id: str, audio_url: str, title: str, type: str = "audio") -> None:
        self.id = id
        self.type = type
        self.audio_url = audio_url
        self.title = title
        self.caption: Optional[str] = None
        self.parse_mode: Optional[str] = None
        self.caption_entities: Optional[list[MessageEntity]] = None
        self.performer: Optional[str] = None
        self.audio_duration: Optional[int] = None
        self.input_message_content: Optional[InputMessageContent] = None
        self.reply_markup: Optional[InlineKeyboardMarkup] = None


class InlineQueryResultVoice(InlineQueryResult):
    """
    Represents a link to a voice recording in an .ogg container encoded with OPUS. 
    By default, this voice recording will be sent by the user. 
    Alternatively, you can use `input_message_content` to send a message with the specified content instead of the the voice message.

    Args:
        type (:obj:`str`): Type of the result, must be voice.

        id (:obj:`str`): Unique identifier for this result, 1-64 bytes.

        voice_url (:obj:`str`): A valid URL for the voice recording.

        title (:obj:`str`): Recording title.

        caption (:obj:`str`, optional): Caption, 0-1024 characters after entities parsing.

        parse_mode (:obj:`str`, optional): Mode for parsing entities in the voice message caption. 
        See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.

        caption_entities (:obj:`list` of :obj:`MessageEntity`, optional): List of special entities that 
        appear in the caption, which can be specified instead of parse_mode.

        voice_duration (:obj:`int`, optional): Recording duration in seconds.

        input_message_content (:obj:`InputMessageContent`, optional): Content of the message to be sent instead of the voice recording.

        reply_markup (:obj:`InlineKeyboardMarkup`, optional): Inline keyboard attached to the message.
    """
    __slots__ = ("type",
                "id",
                "voice_url",
                "title",
                "caption",
                "parse_mode",
                "caption_entities",
                "voice_duration",
                "input_message_content",
                "reply_markup",
                )

    def __init__ (self, id: str, voice_url: str, title: str, type: str = "voice") -> None:
        self.id = id
        self.type = type
        self.voice_url = voice_url
        self.title = title
        self.caption: Optional[str] = None
        self.parse_mode: Optional[str] = None
        self.caption_entities: Optional[list[MessageEntity]] = None
        self.voice_duration: Optional[int] = None
        self.input_message_content: Optional[InputMessageContent] = None


class InlineQueryResultDocument(InlineQueryResult):
    """
    Represents a link to a file. By default, this file will be sent by the user with an optional caption. 
    Alternatively, you can use `input_message_content` to send a message with the specified content instead of the file. 
    Currently, only .PDF and .ZIP files can be sent using this method.

    Args:
        type (:obj:`str`): Type of the result, must be document.

        id (:obj:`str`): Unique identifier for this result, 1-64 bytes.

        title (:obj:`str`): Title for the result.

        caption (:obj:`str`, optional): Caption of the document to be sent, 0-1024 characters after entities parsing.

        parse_mode (:obj:`str`, optional): Mode for parsing entities in the document caption. 
        See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.

        caption_entities (:obj:`list` of :obj:`MessageEntity`, optional): List of special entities that 
        appear in the caption, which can be specified instead of parse_mode.

        document_url (:obj:`str`): A valid URL for the file.

        mime_type (:obj:`str`): Mime type of the content of the file, either “application/pdf” or “application/zip”.

        description (:obj:`str`, optional): Short description of the result.

        input_message_content (:obj:`InputMessageContent`, optional): Content of the message to be sent instead of the file.

        reply_markup (:obj:`InlineKeyboardMarkup`, optional): Inline keyboard attached to the message.

        thumb_url (:obj:`str`, optional): URL of the thumbnail (jpeg only) for the file.

        thumb_width (:obj:`int`, optional): Thumbnail width.

        thumb_height (:obj:`int`, optional): Thumbnail height.
    """
    __slots__ = ("type",
                "id",
                "title",
                "caption",
                "parse_mode",
                "caption_entities",
                "document_url",
                "mime_type",
                "description",
                "input_message_content",
                "reply_markup",
                "thumb_url",
                "thumb_width",
                "thumb_height",
                )

    def __init__ (self, id: str, title: str, document_url: str, mime_type: str, type: str = "document") -> None:
        self.id = id
        self.type = type
        self.title = title
        self.caption: Optional[str] = None
        self.parse_mode: Optional[str] = None
        self.caption_entities: Optional[list[MessageEntity]] = None
        self.document_url = document_url
        self.mime_type = mime_type
        self.description: Optional[str] = None
        self.input_message_content: Optional[InputMessageContent] = None
        self.reply_markup: Optional[InlineKeyboardMarkup] = None
        self.thumb_url: Optional[str] = None
        self.thumb_width: Optional[int] = None
        self.thumb_height: Optional[int] = None



class InlineQueryResultLocation(InlineQueryResult):
    """
    Represents a location on a map. By default, the location will be sent by the user. 
    Alternatively, you can use `input_message_content` to send a message with the specified content instead of the location.

    Args:
        type (:obj:`str`): Type of the result, must be location.

        id (:obj:`str`): Unique identifier for this result, 1-64 Bytes.

        latitude (:obj:`float`): Location latitude in degrees.

        longitude (:obj:`float`): Location longitude in degrees.

        title (:obj:`str`): Location title.

        horizontal_accuracy (:obj:`float`, optional): The radius of uncertainty for the location, measured in meters; 0-1500.

        live_period (:obj:`int`, optional): Period in seconds for which the location can be updated, should be between 60 and 86400.

        heading (:obj:`int`, optional): For live locations, a direction in which the user is moving, in degrees. 
        Must be between 1 and 360 if specified.

        proximity_alert_radius (:obj:`int`, optional): For live locations, a maximum distance for proximity alerts about approaching another chat member, 
        in meters. Must be between 1 and 100000 if specified.

        input_message_content (:obj:`InputMessageContent`, optional): Content of the message to be sent instead of the location.

        reply_markup (:obj:`InlineKeyboardMarkup`, optional): Inline keyboard attached to the message.

        thumb_url (:obj:`str`, optional): Url of the thumbnail for the result.

        thumb_width (:obj:`int`, optional): Thumbnail width.

        thumb_height (:obj:`int`, optional): Thumbnail height.
    """
    __slots__ = ("type",
                "id",
                "latitude",
                "longitude",
                "title",
                "horizontal_accuracy",
                "live_period",
                "heading",
                "proximity_alert_radius",
                "input_message_content",
                "reply_markup",
                "thumb_url",
                "thumb_width",
                "thumb_height",
                )

    def __init__ (self, id: str, latitude: float, longitude: float, title: str, type: str = "location") -> None:
        self.id = id
        self.type = type
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.horizontal_accuracy: Optional[float] = None
        self.live_period: Optional[int] = None
        self.heading: Optional[int] = None
        self.proximity_alert_radius: Optional[int] = None
        self.input_message_content: Optional[InputMessageContent] = None
        self.reply_markup: Optional[InlineKeyboardMarkup] = None
        self.thumb_url: Optional[str] = None
        self.thumb_width: Optional[int] = None
        self.thumb_height: Optional[int] = None


class InlineQueryResultVenue(InlineQueryResult):
    """
    Represents a venue. By default, the venue will be sent by the user. 
    Alternatively, you can use `input_message_content` to send a message with the specified content instead of the venue.

    Args:
        type (:obj:`str`): Type of the result, must be venue.

        id (:obj:`str`): Unique identifier for this result, 1-64 Bytes.

        latitude (:obj:`float`): Latitude of the venue location in degrees.

        longitude (:obj:`float`): Longitude of the venue location in degrees.

        title (:obj:`str`): Title of the venue.

        address (:obj:`str`): Address of the venue.

        foursquare_id (:obj:`str`, optional): Foursquare identifier of the venue if known.

        foursquare_type (:obj:`str`, optional): Foursquare type of the venue, if known. 
        (For example, “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)

        google_place_id (:obj:`str`, optional): Google Places identifier of the venue.

        google_place_type (:obj:`str`, optional): Google Places type of the venue. 
        (See `supported types <https://developers.google.com/places/web-service/supported_types>`_.)

        input_message_content (:obj:`InputMessageContent`, optional): Content of the message to be sent instead of the venue.

        reply_markup (:obj:`InlineKeyboardMarkup`, optional): Inline keyboard attached to the message.

        thumb_url (:obj:`str`, optional): Url of the thumbnail for the result.

        thumb_width (:obj:`int`, optional): Thumbnail width.

        thumb_height (:obj:`int`, optional): Thumbnail height.
    """
    __slots__ = ("type",
                "id",
                "latitude",
                "longitude",
                "title",
                "address",
                "foursquare_id",
                "foursquare_type",
                "google_place_id",
                "google_place_type",
                "input_message_content",
                "reply_markup",
                "thumb_url",
                "thumb_width",
                "thumb_height",
                )

    def __init__ (self, id: str, latitude: float, longitude: float, title: str, address: str, type: str = "venue") -> None:
        self.id = id
        self.type = type
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.address = address
        self.foursquare_id: Optional[str] = None
        self.foursquare_type: Optional[str] = None
        self.google_place_id: Optional[str] = None
        self.google_place_type: Optional[str] = None
        self.input_message_content: Optional[InputMessageContent] = None
        self.reply_markup: Optional[InlineKeyboardMarkup] = None
        self.thumb_url: Optional[str] = None
        self.thumb_width: Optional[int] = None
        self.thumb_height: Optional[int] = None



class InlineQueryResultContact(InlineQueryResult):
    """
    Represents a contact with a phone number. By default, this contact will be sent by the user. 
    Alternatively, you can use `input_message_content` to send a message with the specified content instead of the contact.

    Args:
        type (:obj:`str`): Type of the result, must be contact.

        id (:obj:`str`): Unique identifier for this result, 1-64 Bytes.

        phone_number (:obj:`str`): Contact's phone number.

        first_name (:obj:`str`): Contact's first name.

        last_name (:obj:`str`, optional): Contact's last name.

        vcard (:obj:`str`, optional): Additional data about the contact in the form of a vCard, 0-2048 bytes.

        input_message_content (:obj:`InputMessageContent`, optional): Content of the message to be sent instead of the contact.

        reply_markup (:obj:`InlineKeyboardMarkup`, optional): Inline keyboard attached to the message.

        thumb_url (:obj:`str`, optional): Url of the thumbnail for the result.

        thumb_width (:obj:`int`, optional): Thumbnail width.

        thumb_height (:obj:`int`, optional): Thumbnail height.
    """
    __slots__ = ("type",
                "id",
                "phone_number",
                "first_name",
                "last_name",
                "vcard",
                "input_message_content",
                "reply_markup",
                "thumb_url",
                "thumb_width",
                "thumb_height",
                )

    def __init__ (self, id: str, phone_number: str, first_name: str, type: str = "contact") -> None:
        self.id = id
        self.type = type
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name: Optional[str] = None
        self.vcard: Optional[str] = None
        self.input_message_content: Optional[InputMessageContent] = None
        self.reply_markup: Optional[InlineKeyboardMarkup] = None
        self.thumb_url: Optional[str] = None
        self.thumb_width: Optional[int] = None
        self.thumb_height: Optional[int] = None


class InlineQueryResultGame(InlineQueryResult):
    """
    Represents a Game.

    Args:
        type (:obj:`str`): Type of the result, must be game.

        id (:obj:`str`): Unique identifier for this result, 1-64 bytes.

        game_short_name (:obj:`str`): Short name of the game.

        reply_markup (:obj:`InlineKeyboardMarkup`, optional): Inline keyboard attached to the message.
    """
    __slots__ = ("type",
                "id",
                "game_short_name",
                "reply_markup",
                )

    def __init__ (self, id: str, game_short_name: str, type: str = "game") -> None:
        self.id = id
        self.type = type
        self.game_short_name = game_short_name
        self.reply_markup: Optional[InlineKeyboardMarkup] = None


class ChosenInlineResult(InlineQueryResult):
    """
    This object represents a result of an inline query that was chosen by the user and sent to their chat partner.

    Args:
        result_id (:obj:`str`): The unique identifier for the result that was chosen.

        from_user (:obj:`User`): The user that chose the result.

        location (:obj:`Location`, optional): Sender location, only for bots that require user location.

        inline_message_id (:obj:`str`, optional): Identifier of the sent inline message. 
        Available only if there is an inline keyboard attached to the message. 
        Will be also received in callback queries and can be used to edit the message.

        query (:obj:`str`): The query that was used to obtain the result.
    """
    __slots__ = ("result_id",
                "from_user",
                "location",
                "inline_message_id",
                "query",
                )

    def __init__ (self, result_id: str, from_user: User, query: str) -> None:
        self.result_id = result_id
        self.from_user = from_user
        self.location: Optional[Location] = None
        self.inline_message_id: Optional[str] = None
        self.query = query