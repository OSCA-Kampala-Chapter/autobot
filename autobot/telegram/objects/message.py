from .base import BaseObject
from .audio import Audio
from .animation import Animation
from .chat import Chat
from .contact import Contact
from .dice import Dice
from .document import Document
from ..games.objects import Game
from ..inline.objects import InlineKeyboardMarkup
from .location import Location
from .photosize import PhotoSize
from .poll import Poll
from .proximityalerttriggered import ProximityAlertTriggered
from passport.objects import PassportData
from payments.objects import SuccessfulPayment, Invoice
from stickers.objects import Sticker
from .user import User
from .venue import Venue
from .video import Video, VideoNote, VideoChatStarted, VideoChatEnded, VideoChatParticipantsInvited, VideoChatScheduled
from .voice import Voice




from typing import Optional

class Message(BaseObject):
    """
    This object represents a message.

    Args:
        message_id (int): Unique message identifier inside this chat
        from_user (:class:`telegram.User`): Optional. Sender, can be empty for messages sent to channels
        date (:class:`datetime.datetime`): Date the message was sent in Unix time
        chat (:class:`telegram.Chat`): Conversation the message belongs to
        forward_from (:class:`telegram.User`): Optional. For forwarded messages, sender of the original message
        forward_from_chat (:class:`telegram.Chat`): Optional. For messages forwarded from a channel, information about the original channel
        forward_from_message_id (int): Optional. For messages forwarded from channels, identifier of the original message in the channel
        forward_signature (str): Optional. For messages forwarded from channels, signature of the post author if present
        forward_sender_name (str): Optional. Sender's name for messages forwarded from users who disallow adding a link to their account in forwarded messages
        forward_date (:class:`datetime.datetime`): Optional. For forwarded messages, date the original message was sent in Unix time
        reply_to_message (:class:`telegram.Message`): Optional. For replies, the original message. Note that the Message object in this field will not contain further reply_to_message fields even if it itself is a reply.
        via_bot (:class:`telegram.User`): Optional. Bot through which the message was sent
        edit_date (:class:`datetime.datetime`): Optional. Date the message was last edited in Unix time
        media_group_id (str): Optional. The unique identifier of a media message group this message belongs to
        author_signature (str): Optional. Signature of the post author for messages in channels
        text (str): Optional. For text messages, the actual UTF-8 text of the message, 0-4096 characters.
        entities (List[:class:`telegram.MessageEntity`]): Optional. For text messages, special entities like usernames, URLs, bot commands, etc. that appear in the text
        caption_entities (List[:class:`telegram.MessageEntity`]): Optional. For messages with a caption, special entities like usernames, URLs, bot commands, etc. that appear in the caption
        audio (:class:`telegram.Audio`): Optional. Message is an audio file, information about the file
        document (:class:`telegram.Document`): Optional. Message is a general file, information about the file
        animation (:class:`telegram.Animation`): Optional. Message is an animation, information about the animation. For backward compatibility, when this field is set, the document field will also be set
        game (:class:`telegram.Game`): Optional. Message is a game, information about the game. More about games »
        photo (List[:class:`telegram.PhotoSize`]): Optional. Message is a photo, available sizes of the photo
        sticker (:class:`telegram.Sticker`): Optional. Message is a sticker, information about the sticker
        video (:class:`telegram.Video`): Optional. Message is a video, information about the video
        voice (:class:`telegram.Voice`): Optional. Message is a voice message, information about the file
        video_note (:class:`telegram.VideoNote`): Optional. Message is a video note, information about the video message
        caption (str): Optional. Caption for the animation, audio, document, photo, video or voice, 0-1024 characters
        contact (:class:`telegram.Contact`): Optional. Message is a shared contact, information about the contact
        location (:class:`telegram.Location`): Optional. Message is a shared location, information about the location
        venue (:class:`telegram.Venue`): Optional. Message is a venue, information about the venue. For backward compatibility, when this field is set, the location field will also be set
        poll (:class:`telegram.Poll`): Optional. Message is a native poll, information about the poll
        dice (:class:`telegram.Dice`): Optional. Message is a dice with random value from 1 to 6
        new_chat_members (List[:class:`telegram.User`]): Optional. New members that were added to the group or supergroup and information about them (the bot itself may be one of these members)
        left_chat_member (:class:`telegram.User`): Optional. A member was removed from the group, information about them (this member may be the bot itself)
        new_chat_title (str): Optional. A chat title was changed to this value
        new_chat_photo (List[:class:`telegram.PhotoSize`]): Optional. A chat photo was change to this value
        delete_chat_photo (bool): Optional. Service message: the chat photo was deleted
        group_chat_created (bool): Optional. Service message: the group has been created
        supergroup_chat_created (bool): Optional .Service message: the supergroup has been created. This field can't be received in a message coming through updates, because bot can't be a member of a supergroup when it is created. It can only be found in reply_to_message if someone replies to a very first message in a directly created supergroup.
        channel_chat_created (bool): Optional. Service message: the channel has been created. This field can't be received in a message coming through updates, because bot can't be a member of a channel when it is created. It can only be found in reply_to_message if someone replies to a very first message in a channel.
        migrate_to_chat_id (int): Optional. The group has been migrated to a supergroup with the specified identifier. This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier.
        migrate_from_chat_id (int): Optional. The supergroup has been migrated from a group with the specified identifier. This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier.
        pinned_message (:class:`telegram.Message`): Optional. Specified message was pinned. Note that the Message object in this field will not contain further reply_to_message fields even if it is itself a reply.
        invoice (:class:`telegram.Invoice`): Optional. Message is an invoice for a payment, information about the invoice. More about payments »
        successful_payment (:class:`telegram.SuccessfulPayment`): Optional. Message is a service message about a successful payment, information about the payment. More about payments »
        connected_website (str): Optional. The domain name of the website on which the user has logged in. More about Telegram Login »
        passport_data (:class:`telegram.PassportData`): Optional. Telegram Passport data
        proximity_alert_triggered (:class:`telegram.ProximityAlertTriggered`): Optional. Service message. A user in the chat triggered another user's proximity alert while sharing Live Location.
        video_chat_scheduled (:class:`telegram.VideoChatScheduled`): Optional. Service message: voice chat scheduled
        video_chat_started (:class:`telegram.VideoChatStarted`): Optional. Service message: voice chat started
        video_chat_ended (:class:`telegram.VideoChatEnded`): Optional. Service message: voice chat ended
        video_chat_participants_invited (:class:`telegram.VideoChatParticipantsInvited`): Optional. Service message: new participants invited to a voice chat
        reply_markup (:class:`telegram.InlineKeyboardMarkup`): Optional. Inline keyboard attached to the message. login_url buttons are represented as ordinary url buttons.
    """
    __slots__ = (
        'message_id',
        'from_user',
        'date',
        'chat',
        'forward_from',
        'forward_from_chat',
        'forward_from_message_id',
        'forward_signature',
        'forward_sender_name',
        'forward_date',
        'reply_to_message',
        'via_bot',
        'edit_date',
        'media_group_id',
        'author_signature',
        'text',
        'entities',
        'caption_entities',
        'audio',
        'document',
        'animation',
        'game',
        'photo',
        'sticker',
        'video',
        'voice',
        'video_note',
        'caption',
        'contact',
        'location',
        'venue',
        'poll',
        'dice',
        'new_chat_members',
        'left_chat_member',
        'new_chat_title',
        'new_chat_photo',
        'delete_chat_photo',
        'group_chat_created',
        'supergroup_chat_created',
        'channel_chat_created',
        'migrate_to_chat_id',
        'migrate_from_chat_id',
        'pinned_message',
        'invoice',
        'successful_payment',
        'connected_website',
        'passport_data',
        'proximity_alert_triggered',
        'video_chat_scheduled',
        'video_chat_started',
        'video_chat_ended',
        'video_chat_participants_invited',
        'reply_markup'
    )
    
    def __init__ (self, message_id: int) -> None:
        self.message_id = message_id
        self.from_user: Optional[User] = None
        self.date: Optional[int] = None
        self.chat: Optional[Chat] = None
        self.forward_from: Optional[User] = None
        self.forward_from_chat: Optional[Chat] = None
        self.forward_from_message_id: Optional[int] = None
        self.forward_signature: Optional[str] = None
        self.forward_sender_name: Optional[str] = None
        self.forward_date: Optional[int] = None
        self.reply_to_message: Optional[Message] = None
        self.via_bot: Optional[User] = None
        self.edit_date: Optional[int] = None
        self.media_group_id: Optional[str] = None
        self.author_signature: Optional[str] = None
        self.text: Optional[str] = None
        self.entities: Optional[list[MessageEntity]] = None
        self.caption_entities: Optional[list[MessageEntity]] = None 
        self.audio: Optional[Audio] = None
        self.document: Optional[Document] = None
        self.animation: Optional[Animation] = None
        self.game: Optional[Game] = None
        self.photo: Optional[list[PhotoSize]] = None
        self.sticker: Optional[Sticker] = None
        self.video: Optional[Video] = None
        self.voice: Optional[Voice] = None
        self.video_note: Optional[VideoNote] = None
        self.caption: Optional[str] = None
        self.contact: Optional[Contact] = None
        self.location: Optional[Location] = None
        self.venue: Optional[Venue] = None
        self.poll: Optional[Poll] = None
        self.dice: Optional[Dice] = None
        self.new_chat_members: Optional[list[User]] = None
        self.left_chat_member: Optional[User] = None
        self.new_chat_title: Optional[str] = None
        self.new_chat_photo: Optional[list[PhotoSize]] = None
        self.delete_chat_photo: Optional[bool] = None
        self.group_chat_created: Optional[bool] = None
        self.supergroup_chat_created: Optional[bool] = None
        self.channel_chat_created: Optional[bool] = None
        self.migrate_to_chat_id: Optional[int] = None
        self.migrate_from_chat_id: Optional[int] = None
        self.pinned_message: Optional[Message] = None
        self.invoice: Optional[Invoice] = None
        self.successful_payment: Optional[SuccessfulPayment] = None
        self.connected_website: Optional[str] = None
        self.passport_data: Optional[PassportData] = None
        self.proximity_alert_triggered: Optional[ProximityAlertTriggered] = None
        self.video_chat_scheduled: Optional[VideoChatScheduled] = None
        self.video_chat_started: Optional[VideoChatStarted] = None
        self.video_chat_ended: Optional[VideoChatEnded] = None
        self.video_chat_participants_invited: Optional[VideoChatParticipantsInvited] = None
        self.reply_markup: Optional[InlineKeyboardMarkup] = None

class MessageAutoDeleteTimerChanged(BaseObject):
    """This object represents a service message about a change in auto-delete timer settings.

    Args:
        message (:class:`telegram.Message`): The message with the change.
        message_auto_delete_time (:class:`telegram.MessageAutoDeleteTimerChanged`): New auto-delete time for messages in the chat.

    Attributes:
        message (:class:`telegram.Message`): The message with the change.
        message_auto_delete_time (:class:`telegram.MessageAutoDeleteTimerChanged`): New auto-delete time for messages in the chat.

    """

    __slots__ = ("message","message_auto_delete_time")
    
    def __init__(self, message, message_auto_delete_time):
        self.message = message
        self.message_auto_delete_time = message_auto_delete_time


class MessageEntity(BaseObject):
    """
    This object represents one special entity in a text message. For example, hashtags, usernames, URLs, etc.

    Args:
        type (str): Type of the entity. Can be mention (@username), hashtag, cashtag, bot_command, 
        url, email, phone_number, bold (bold text), italic (italic text), code (monowidth string), 
        pre (monowidth block), text_link (for clickable text URLs), text_mention (for users without usernames)

        offset (int): Offset in UTF-16 code units to the start of the entity
        length (int): Length of the entity in UTF-16 code units
        url (str): Optional. For “text_link” only, url that will be opened after user taps on the text
        user (:class:`telegram.User`): Optional. For “text_mention” only, the mentioned user
        language (str): Optional. For “pre” only, the programming language of the entity text
        custom_emoji_id (str): Optional. For “custom_emoji” only, the custom emoji id

    """

    __slots__ = (
        'type',
        'offset',
        'length',
        'url', 
        'user', 
        'language'
        )

    def __init__(self, type: str, offset: int, length: int) -> None:
        self.type = type
        self.offset = offset
        self.length = length
        self.url: Optional[str] = None
        self.user: Optional[User] = None
        self.language: Optional[str] = None

class MessageId(BaseObject):
    """
    This object represents a unique message identifier.

    Args:
        message_id (int): Unique message identifier

    """
    
    __slots__ = ("message_id")
    
    def __init__(self, message_id):
        self.message_id = message_id
        
