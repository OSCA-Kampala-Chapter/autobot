from ..objects import BaseObject

class InlineQuery(BaseObject):
    
    __slots__ = ("id",
                "from_",
                "query",
                "offset",
                "chat_type",
                "location",
                )
    def __init__(self,id,from_,query,offset):
        self.id = id
        self.from_ = from_
        self.query = query
        self.offset = offset
        self.chat_type = chat_type
        self.location = location
        
class InlineQueryResult (BaseObject):
    """
    Base class for InlineQueryResult* objects.
    """
    __slots__ = ("type",
                "id",
                )
    def __init__ (self,type,id):
        self.type = type
        self.id = id
        


class InlineQueryResultCachedAudio(BaseObject):
    """
    Represents a link to an mp3 audio file stored on the Telegram servers. 
    By default, this audio file will be sent by the user. 
    Alternatively, you can use `input_message_content` to 
    send a message with the specified content instead of the audio.

    Args:
        type (:obj:`str`): Type of the result, must be audio.
        id (:obj:`str`): Unique identifier for this result, 1-64 bytes.
        audio_file_id (:obj:`str`): A valid file identifier for the audio file.
        caption (:obj:`str`, optional): Caption, 0-1024 characters after entities parsing.
        parse_mode (:obj:`str` | :class:`telegram.ParseMode`, optional): Mode for parsing entities in the audio caption. See
            :class:`telegram.ParseMode` for more details.

    Keyword Args:
        caption_entities (:obj:`list` of :class:`telegram.MessageEntity`, optional): List of special
            entities that appear in the caption, which can be specified instead of
            `parse_mode`.
        input_message_content (:class:`telegram.InputMessageContent`, optional): Content of the message to be sent instead of the audio.
        reply_markup (:class:`telegram.InlineKeyboardMarkup`, optional): Inline keyboard attached to the message.
        url (:obj:`str`, optional): URL of the result.
        hide_url (:obj:`bool`, optional): Pass True, if you don't want the URL to be shown in the message.
        title (:obj:`str`, optional): Title for the result.
        description (:obj:`str`, optional): Short description of the result.
        thumb_url (:obj:`str`, optional): URL of the thumbnail (jpeg only) for the file.
        thumb_width (:obj:`int`, optional): Thumbnail width.
        thumb_height (:obj:`int`, optional): Thumbnail height.

    """
    __slots__ = (
        "type",
        "id",
        "audio_file_id",
        "caption",
        "parse_mode",
        "caption_entities",
        "input_message_content",
        "reply_markup",
        "url",
        "hide_url",
        "title",
        "description",
        "thumb_url",
        "thumb_width",
        "thumb_height",
    )
                

    def __init__ (self,type,id,audio_file_id):
        self.type = type
        self.id = id
        self.audio_file_id = audio_file_id
        self.caption = None
        self.parse_mode = None
        self.caption_entities = None
        self.input_message_content = None
        self.reply_markup = None
        self.url = None
        self.hide_url = None
        self.title = None
        self.description = None
        self.thumb_url = None
        self.thumb_width = None
        self.thumb_height = None


class InlineQueryResultCachedDocument(BaseObject):
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
        parse_mode (:obj:`str` | :class:`telegram.ParseMode`, optional): Mode for parsing entities in the document caption. See
            :class:`telegram.ParseMode` for more details.

    Keyword Args:
        caption_entities (:obj:`list` of :class:`telegram.MessageEntity`, optional): List of special
            entities that appear in the caption, which can be specified instead of
            `parse_mode`.
        input_message_content (:class:`telegram.InputMessageContent`, optional): Content of the message to be sent instead of the file.
        reply_markup (:class:`telegram.InlineKeyboardMarkup`, optional): Inline keyboard attached to the message.
        url (:obj:`str`, optional): URL of the result.
        hide_url (:obj:`bool`, optional): Pass True, if you don't want the URL to be shown in the message.
        thumb_url (:obj:`str`, optional): URL of the thumbnail (jpeg only) for the file.
        thumb_width (:obj:`int`, optional): Thumbnail width.
        thumb_height (:obj:`int`, optional): Thumbnail height.

    """
    __slots__ = (
        "type",
        "id",
        "title",
        "document_file_id",
        "description",
        "caption",
        "parse_mode",
        "caption_entities",
        "input_message_content",
        "reply_markup",
        "url",
        "hide_url",
        "thumb_url",
        "thumb_width",
        "thumb_height",
    )

    def __init__ (self,type,id,title,document_file_id):
        self.type = type
        self.id = id
        self.title = title
        self.document_file_id = document_file_id
        self.description = None
        self.caption = None
        self.parse_mode = None
        self.caption_entities = None
        self.input_message_content = None
        self.reply_markup = None
        self.url = None
        self.hide_url = None
        self.thumb_url = None
        self.thumb_width = None
        self.thumb_height = None


class InlineQueryResultCachedGif(BaseObject):
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
        parse_mode (:obj:`str` | :class:`telegram.ParseMode`, optional): Mode for parsing entities in the animation caption. See
            :class:`telegram.ParseMode` for more details.

    Keyword Args:
        caption_entities (:obj:`list` of :class:`telegram.MessageEntity`, optional): List of special
            entities that appear in the caption, which can be specified instead of
            `parse_mode`.
        input_message_content (:class:`telegram.InputMessageContent`, optional): Content of the message to be sent instead of the GIF animation.
        reply_markup (:class:`telegram.InlineKeyboardMarkup`, optional): Inline keyboard attached to the message.
        url (:obj:`str`, optional): URL of the result.
        hide_url (:obj:`bool`, optional): Pass True, if you don't want the URL to be shown in the message.
        thumb_url (:obj:`str`, optional): URL of the static thumbnail for the result (jpeg or gif).
        thumb_mime_type (:obj:`str`, optional): MIME type of the thumbnail, must be one of “image/jpeg”, “image/gif”, or “video/mp4”. Defaults to “image/jpeg”.
        thumb_width (:obj:`int`, optional): Thumbnail width.
        thumb_height (:obj:`int`, optional): Thumbnail height.

    """
    __slots__ = (
        "type",
        "id",
        "gif_file_id",
        "title",
        "caption",
        "parse_mode",
        "caption_entities",
        "input_message_content",
        "reply_markup",
        "url",
        "hide_url",
        "thumb_url",
        "thumb_mime_type",
        "thumb_width",
        "thumb_height",
    )

    def __init__ (self,type,id,gif_file_id):
        self.type = type
        self.id = id
        self.gif_file_id = gif_file_id
        self.title = None
        self.caption = None
        self.parse_mode = None
        self.caption_entities = None
        self.input_message_content = None
        self.reply_markup = None
        self.url = None
        self.hide_url = None
        self.thumb_url = None
        self.thumb_mime_type = None
        self.thumb_width = None
        self.thumb_height = None


class InlineQueryResultCachedMpeg4Gif(BaseObject):
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
        parse_mode (:obj:`str` | :class:`telegram.ParseMode`, optional): Mode for parsing entities in the animation caption. See
            :class:`telegram.ParseMode` for more details.

    Keyword Args:
        caption_entities (:obj:`list` of :class:`telegram.MessageEntity`, optional): List of special
            entities that appear in the caption, which can be specified instead of
            `parse_mode`.
        input_message_content (:class:`telegram.InputMessageContent`, optional): Content of the message to be sent instead of the video animation.
        reply_markup (:class:`telegram.InlineKeyboardMarkup`, optional): Inline keyboard attached to the message.
        url (:obj:`str`, optional): URL of the result.
        hide_url (:obj:`bool`, optional): Pass True, if you don't want the URL to be shown in the message.
        thumb_url (:obj:`str`, optional): URL of the static thumbnail (jpeg or gif) for the result.
        thumb_mime_type (:obj:`str`, optional): MIME type of the thumbnail, must be one of “image/jpeg”, “image/gif”, or “video/mp4”. Defaults to “image/jpeg”.
        thumb_width (:obj:`int`, optional): Thumbnail width.
        thumb_height (:obj:`int`, optional): Thumbnail height.

    """
    __slots__ = (
        "type",
        "id",
        "mpeg4_file_id",
        "title",
        "caption",
        "parse_mode",
        "caption_entities",
        "input_message_content",
        "reply_markup",
        "url",
        "hide_url",
        "thumb_url",
        "thumb_mime_type",
        "thumb_width",
        "thumb_height",
    )

    def __init__ (self,type,id,mpeg4_file_id):
        self.type = type
        self.id = id
        self.mpeg4_file_id = mpeg4_file_id
        self.title = None
        self.caption = None
        self.parse_mode = None
        self.caption_entities = None
        self.input_message_content = None
        self.reply_markup = None
        self.url = None
        self.hide_url = None
        self.thumb_url = None
        self.thumb_mime_type = None
        self.thumb_width = None
        self.thumb_height = None


class InlineQueryResultCachedSticker(BaseObject):
    """
    Represents a link to a sticker stored on the Telegram servers. 
    By default, this sticker will be sent by the user. 
    Alternatively, you can use `input_message_content` to send a message with the specified content instead of the sticker.

    Args:
        type (:obj:`str`): Type of the result, must be sticker.
        id (:obj:`str`): Unique identifier for this result, 1-64 bytes.
        sticker_file_id (:obj:`str`): A valid file identifier of the sticker.

    Keyword Args:
        input_message_content (:class:`telegram.InputMessageContent`, optional): Content of the message to be sent instead of the sticker.
        reply_markup (:class:`telegram.InlineKeyboardMarkup`, optional): Inline keyboard attached to the message.

    """
    __slots__ = (
        "type",
        "id",
        "sticker_file_id",
        "input_message_content",
        "reply_markup",
    )

    def __init__ (self,type,id,sticker_file_id):
        self.type = type
        self.id = id
        self.sticker_file_id = sticker_file_id
        self.input_message_content = None
        self.reply_markup = None


class InlineQueryResultCachedPhoto(BaseObject):
    """
    Represents a link to a photo stored on the Telegram servers. 
    By default, this photo will be sent by the user with an optional caption. 
    Alternatively, you can use `input_message_content` to send a message with the specified content instead of the photo.

    Args:
        type (:obj:`str`): Type of the result, must be photo.
        id (:obj:`str`): Unique identifier for this result, 1-64 bytes.
        photo_file_id (:obj:`str`): A valid file identifier of the photo.

    Keyword Args:
        title (:obj:`str`, optional): Title for the result.
        description (:obj:`str`, optional): Short description of the result.
        caption (:obj:`str`, optional): Caption, 0-1024 characters after entities parsing.
        parse_mode (:obj:`str` | :class:`telegram.ParseMode`, optional): Mode for parsing entities in the photo caption. See
            :class:`telegram.ParseMode` for more details.
        caption_entities (:obj:`list` of :class:`telegram.MessageEntity`, optional): List of special
            entities that appear in the caption, which can be specified instead of
            `parse_mode`.
        input_message_content (:class:`telegram.InputMessageContent`, optional): Content of the message to be sent instead of the photo.
        reply_markup (:class:`telegram.InlineKeyboardMarkup`, optional): Inline keyboard attached to the message.

    """
    __slots__ = (
        "type",
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

    def __init__ (self,type,id,photo_file_id):
        self.type = type
        self.id = id
        self.photo_file_id = photo_file_id
        self.title = None
        self.description = None
        self.caption = None
        self.parse_mode = None
        self.caption_entities = None
        self.input_message_content = None
        self.reply_markup = None


class InlineQueryResultCachedVideo(BaseObject):
    """
    Represents a link to a video file stored on the Telegram servers. 
    By default, this video file will be sent by the user with an optional caption. 
    Alternatively, you can use `input_message_content` to send a message with the specified content instead of the video.

    Args:
        type (:obj:`str`): Type of the result, must be video.
        id (:obj:`str`): Unique identifier for this result, 1-64 bytes.
        video_file_id (:obj:`str`): A valid file identifier for the video file.

    Keyword Args:
        title (:obj:`str`, optional): Title for the result.
        description (:obj:`str`, optional): Short description of the result.
        caption (:obj:`str`, optional): Caption, 0-1024 characters after entities parsing.
        parse_mode (:obj:`str` | :class:`telegram.ParseMode`, optional): Mode for parsing entities in the video caption. See
            :class:`telegram.ParseMode` for more details.
        caption_entities (:obj:`list` of :class:`telegram.MessageEntity`, optional): List of special
            entities that appear in the caption, which can be specified instead of
            `parse_mode`.
        input_message_content (:class:`telegram.InputMessageContent`, optional): Content of the message to be sent instead of the video.
        reply_markup (:class:`telegram.InlineKeyboardMarkup`, optional): Inline keyboard attached to the message.

    """
    __slots__ = (
        "type",
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

    def __init__ (self,type,id,video_file_id):
        self.type = type
        self.id = id
        self.video_file_id = video_file_id
        self.title = None
        self.description = None
        self.caption = None
        self.parse_mode = None
        self.caption_entities = None
        self.input_message_content = None
        self.reply_markup = None

