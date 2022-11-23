
from __future__ import annotations

from autobot.telegram.objects import BaseObject
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from autobot.telegram.objects import User, Location, MessageEntity, InlineKeyboardMarkup
    from autobot.telegram.payments.objects import LabeledPrice


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

class InputTextMessageContent(InputMessageContent):
    """
    Represents the content of a text message to be sent as the result of an inline query.
    
    Args:
        message_text (str): Text of the message to be sent, 1-4096 characters
        parse_mode (str, optional): Mode for parsing entities in the message text. 
            See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.
        disable_web_page_preview (bool, optional): Disables link previews for links in the sent message
        entities (List[:class:`autobot.telegram.objects.MessageEntity`], optional): List of special entities that appear in message text, 
            which can be specified instead of parse_mode
        disable_notification (bool, optional): Sends the message silently. 
            iOS users will not receive a notification, Android users will receive a notification with no sound.
        reply_to_message_id (int, optional): If the message is a reply, ID of the original message
        allow_sending_without_reply (bool, optional): Pass True, if the message should be sent even if the specified replied-to message is not found
        reply_markup (:class:`autobot.telegram.objects.InlineKeyboardMarkup`, optional): Additional interface options. 
            A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
    """
    
    __slots__ = (
        'message_text',
        'parse_mode',
        'disable_web_page_preview',
        'entities',
        'disable_notification',
        'reply_to_message_id',
        'allow_sending_without_reply',
        'reply_markup',
    )

    def __init__(self, message_text: str = None) -> None:
        self.message_text = message_text
        self.parse_mode: Optional[str] = None
        self.disable_web_page_preview: Optional[bool] = None
        self.entities: Optional[list[MessageEntity]] = None
        self.disable_notification: Optional[bool] = None
        self.reply_to_message_id: Optional[int] = None
        self.allow_sending_without_reply: Optional[bool] = None
        self.reply_markup: Optional[InlineKeyboardMarkup] = None


class InputLocationMessageContent(InputMessageContent):
    """
    Represents the content of a location message to be sent as the result of an inline query.
    
    Args:
        latitude (float): Latitude of the location in degrees
        longitude (float): Longitude of the location in degrees
        horizontal_accuracy (float, optional): The radius of uncertainty for the location, measured in meters; 0-1500
        live_period (int, optional): Period in seconds for which the location can be updated, should be between 60 and 86400.
        heading (int, optional): For live locations, a direction in which the user is moving, in degrees. 
            Must be between 1 and 360 if specified.
        proximity_alert_radius (int, optional): For live locations, a maximum distance for proximity alerts about approaching another chat member, 
            in meters. Must be between 1 and 100000 if specified.
    """
    
    __slots__ = (
        'latitude',
        'longitude',
        'horizontal_accuracy',
        'live_period',
        'heading',
        'proximity_alert_radius',
    )

    def __init__(self, latitude: float = None, longitude: float = None) -> None:
        self.latitude = latitude
        self.longitude = longitude
        self.horizontal_accuracy: Optional[float] = None
        self.live_period: Optional[int] = None
        self.heading: Optional[int] = None
        self.proximity_alert_radius: Optional[int] = None


class InputVenueMessageContent(InputMessageContent):
    """
    Represents the content of a venue message to be sent as the result of an inline query.
    
    Args:
        latitude (float): Latitude of the venue in degrees
        longitude (float): Longitude of the venue in degrees
        title (str): Name of the venue
        address (str): Address of the venue
        foursquare_id (str, optional): Foursquare identifier of the venue, if known
        foursquare_type (str, optional): Foursquare type of the venue, if known. 
            (For example, “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)
        google_place_id (str, optional): Google Places identifier of the venue
        google_place_type (str, optional): Google Places type of the venue. 
            (See supported types.)
    """
    
    __slots__ = (
        'latitude',
        'longitude',
        'title',
        'address',
        'foursquare_id',
        'foursquare_type',
        'google_place_id',
        'google_place_type',
    )

    def __init__(self, latitude: float = None, longitude: float = None, title: str = None, address: str = None) -> None:
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.address = address
        self.foursquare_id: Optional[str] = None
        self.foursquare_type: Optional[str] = None
        self.google_place_id: Optional[str] = None
        self.google_place_type: Optional[str] = None


class InputContactMessageContent(InputMessageContent):
    """
    Represents the content of a contact message to be sent as the result of an inline query.
    
    Args:
        phone_number (str): Contact's phone number
        first_name (str): Contact's first name
        last_name (str, optional): Contact's last name
        vcard (str, optional): Additional data about the contact in the form of a vCard, 0-2048 bytes
    """
    
    __slots__ = (
        'phone_number',
        'first_name',
        'last_name',
        'vcard',
    )

    def __init__(self, phone_number: str = None, first_name: str = None) -> None:
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name: Optional[str] = None
        self.vcard: Optional[str] = None



class InputInvoiceMessageContent(InputMessageContent):
    """
    Represents the content of an invoice message to be sent as the result of an inline query.
    
    Args:
        title (str): Product name, 1-32 characters
        description (str): Product description, 1-255 characters
        payload (str): Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your internal processes.
        provider_token (str): Payments provider token, obtained via Botfather
        currency (str): Three-letter ISO 4217 currency code, see more on currencies
        prices (List[:class:`autobot.telegram.objects.LabeledPrice`]): Price breakdown, a list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.)
        max_tip_amount (int, optional): The maximum accepted amount for tips in the smallest units of the currency (integer, not float/double). 
            For example, for a maximum tip of US$ 1.45 pass max_tip_amount = 145. 
            See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
        suggested_tip_amounts (List[int], optional): A JSON-serialized array of suggested amounts of tip in the smallest units of the currency (integer, not float/double). 
            At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount.
        provider_data (str, optional): JSON-encoded data about the invoice, which will be shared with the payment provider. 
            A detailed description of required fields should be provided by the payment provider.
        photo_url (str, optional): URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service. 
            People like it better when they see what they are paying for.
        photo_size (int, optional): Photo size
        photo_width (int, optional): Photo width
        photo_height (int, optional): Photo height
        need_name (bool, optional): Pass True, if you require the user's full name to complete the order
        need_phone_number (bool, optional): Pass True, if you require the user's phone number to complete the order
        need_email (bool, optional): Pass True, if you require the user's email to complete the order
        need_shipping_address (bool, optional): Pass True, if you require the user's shipping address to complete the order
        send_phone_number_to_provider (bool, optional): Pass True, if user's phone number should be sent to provider
        send_email_to_provider (bool, optional): Pass True, if user's email address should be sent to provider
        is_flexible (bool, optional): Pass True, if the final price depends on the shipping method
    """
    
    __slots__ = (
        'title',
        'description',
        'payload',
        'provider_token',
        'currency',
        'prices',
        'max_tip_amount',
        'suggested_tip_amounts',
        'provider_data',
        'photo_url',
        'photo_size',
        'photo_width',
        'photo_height',
        'need_name',
        'need_phone_number',
        'need_email',
        'need_shipping_address',
        'send_phone_number_to_provider',
        'send_email_to_provider',
        'is_flexible',
    )

    def __init__(self, title: str = None, description: str = None, payload: str = None, provider_token: str = None, currency: str = None, prices: list[LabeledPrice] = None) -> None:
        self.title = title
        self.description = description
        self.payload = payload
        self.provider_token = provider_token
        self.currency = currency
        self.prices = prices
        self.max_tip_amount: Optional[int] = None
        self.suggested_tip_amounts: Optional[list[int]] = None
        self.provider_data: Optional[str] = None
        self.photo_url: Optional[str] = None
        self.photo_size: Optional[int] = None
        self.photo_width: Optional[int] = None
        self.photo_height: Optional[int] = None
        self.need_name: Optional[bool] = None
        self.need_phone_number: Optional[bool] = None
        self.need_email: Optional[bool] = None
        self.need_shipping_address: Optional[bool] = None
        self.send_phone_number_to_provider: Optional[bool] = None
        self.send_email_to_provider: Optional[bool] = None
        self.is_flexible: Optional[bool] = None 


class InlineQuery(BaseObject):
    
    __slots__ = ("id",
                "from_",
                "query",
                "offset",
                "chat_type",
                "location",
                )
    def __init__(self, id: str = None, from_: User = None, query: str = None, offset: str = None) -> None:
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
    def __init__ (self, type: str = None, id: str = None) -> None:
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
    
    def __init__ (self, id: str = None, audio_file_id: str = None, type: str = "audio") -> None:
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
    
    def __init__ (self, id: str = None, title: str = None, document_file_id: str = None, type: str = "document") -> None:
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
    
    def __init__ (self, id: str = None, gif_file_id: str = None, type: str = "gif") -> None:
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
    
    def __init__ (self, id: str = None, mpeg4_file_id: str = None, type: str = "mpeg4_gif") -> None:
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
    
    def __init__ (self, id: str = None, sticker_file_id: str = None, type: str = "sticker") -> None:
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
    
    def __init__ (self, id: str = None, photo_file_id: str = None, type: str = "photo") -> None:
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
    
    def __init__ (self, id: str = None, video_file_id: str = None, type: str = "video") -> None:
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
    
    def __init__ (self, id: str = None, voice_file_id: str = None, title: str = None, type: str = "voice") -> None:
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
    
    def __init__ (self, id: str = None, title: str = None, input_message_content: InputMessageContent = None, type: str = "article") -> None:
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
    
    def __init__ (self, id: str = None, photo_url: str = None, thumb_url: str = None, type: str = "photo") -> None:
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
    
    def __init__ (self, id: str = None, gif_url: str = None, thumb_url: str = None, type: str = "gif") -> None:
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
    

    def __init__ (self, id: str = None, mpeg4_url: str = None, thumb_url: str = None, type: str = "mpeg4_gif") -> None:
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
    

    def __init__ (self, id: str = None, video_url: str = None, mime_type: str = None, thumb_url: str = None, title: str = None, type: str = "video") -> None:
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
    

    def __init__ (self, id: str = None, audio_url: str = None, title: str = None, type: str = "audio") -> None:
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
    

    def __init__ (self, id: str = None, voice_url: str = None, title: str = None, type: str = "voice") -> None:
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
    

    def __init__ (self, id: str = None, title: str = None, document_url: str = None, mime_type: str = None, type: str = "document") -> None:
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
    

    def __init__ (self, id: str = None, latitude: float = None, longitude: float = None, title: str = None, type: str = "location") -> None:
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
    

    def __init__ (self, id: str = None, latitude: float = None, longitude: float = None, title: str = None, address: str = None, type: str = "venue") -> None:
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
    

    def __init__ (self, id: str = None, phone_number: str = None, first_name: str = None, type: str = "contact") -> None:
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
    

    def __init__ (self, id: str = None, game_short_name: str = None, type: str = "game") -> None:
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
    

    def __init__ (self, result_id: str =None, from_user: User =None, query: str =None) -> None:
        self.result_id = result_id
        self.from_user = from_user
        self.location: Optional[Location] = None
        self.inline_message_id: Optional[str] = None
        self.query = query