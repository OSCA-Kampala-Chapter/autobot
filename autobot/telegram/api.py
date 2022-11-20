"""
This module contains a class having methods representing the bot api methods
"""
from autobot.telegram.objects.chat import ChatPermissions
from autobot.telegram.objects.inlinekeyboard import InlineKeyboardMarkup
from autobot.telegram.objects.inputfile import (
    InputFile,
    InputMediaAudio,
    InputMediaDocument,
    InputMediaPhoto,
    InputMediaVideo,
)
from autobot.telegram.objects.message import MessageEntity
from autobot.telegram.objects.replykeyboard import (
    ForceReply,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)


class BotAPI:

    def get_me(self):
        """A simple method for testing your bot's authentication token. Requires no parameters. Returns basic information about the bot in form of a User object.
        """
        pass

    def logout(self):
        """Use this method to log out from the cloud Bot API server before launching the bot locally. You must log out the bot before running it locally, otherwise there is no guarantee that the bot will receive updates. After a successful call, you can immediately log in on a local server, but will not be able to log in back to the cloud Bot API server for 10 minutes. Returns True on success. Requires no parameters.
        """
        pass

    def close(self):
        """Use this method to close the bot instance before moving it from one local server to another. You need to delete the webhook before calling this method to ensure that the bot isn't launched again after server restart. The method will return error 429 in the first 10 minutes after the bot is launched. Returns True on success. Requires no parameters.
        """
        pass

    def send_message(self, chat_id: int | str, text: str, message_thread_id: int | None = None,
                     parse_mode: str | None = None, entities: list[MessageEntity] | None = None,
                     disable_web_page_preview: bool | None = None, disable_notification: bool | None = None,
                     protect_content: bool | None = None, reply_to_message_id: int | None = None,
                     allow_sending_without_reply: bool | None = None,
                     reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply | None = None):
        """Use this method to send text messages. On success, the sent Message is returned.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
            text (str): Text of the message to be sent, 1-4096 characters after entities parsing
            message_thread_id (int | None, optional): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only. Defaults to None.
            parse_mode (str | None, optional): Mode for parsing entities in the message text. Defaults to None.
            entities (list[MessageEntity] | None, optional): A JSON-serialized list of special entities that appear in message text, which can be specified instead of parse_mode. Defaults to None.
            disable_web_page_preview (bool | None, optional): Disables link previews for links in this message. Defaults to None.
            disable_notification (bool | None, optional): Sends the message silently. Users will receive a notification with no sound. Defaults to None.
            protect_content (bool | None, optional): Protects the contents of the sent message from forwarding and saving. Defaults to None.
            reply_to_message_id (int | None, optional): If the message is a reply, ID of the original message. Defaults to None.
            allow_sending_without_reply (bool | None, optional): Pass True if the message should be sent even if the specified replied-to message is not found. Defaults to None.
            reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply, optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user. Defaults to None.
        """
        pass

    def foward_message(self, chat_id: int | str, from_chat_id: int | str, message_id: int,
                       message_thread_id: int | None = None, disable_notification: bool | None = None,
                       protect_content: int | None = None):
        """Use this method to forward messages of any kind. Service messages can't be forwarded. On success, the sent Message is returned.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
            from_chat_id (int | str): Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername)
            message_id (int): Message identifier in the chat specified in from_chat_id
            message_thread_id (int | None, optional): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only. Defaults to None.
            disable_notification (bool | None, optional): Sends the message silently. Users will receive a notification with no sound. Defaults to None.
            protect_content (int | None, optional): Protects the contents of the forwarded message from forwarding and saving. Defaults to None.
        """
        pass

    def copy_message(self, chat_id: int | str, from_chat_id: int | str, message_id: int | str,
                     message_thread_id: int | None = None, caption: str | None = None, parse_mode: str | None = None,
                     caption_entities: list[MessageEntity] | None = None, disable_notification: bool | None = None,
                     protect_content: bool | None = None, reply_to_message_id: bool | None = None,
                     allow_sending_without_reply: bool | None = None,
                     reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply | None = None):
        """Use this method to copy messages of any kind. Service messages and invoice messages can't be copied. A quiz poll can be copied only if the value of the field correct_option_id is known to the bot. The method is analogous to the method forwardMessage, but the copied message doesn't have a link to the original message. Returns the MessageId of the sent message on success.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
            from_chat_id (int | str):  	Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername)
            message_id (int | str): Message identifier in the chat specified in from_chat_id
            message_thread_id (int | None, optional): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only. Defaults to None.
            caption (str | None, optional): New caption for media, 0-1024 characters after entities parsing. If not specified, the original caption is kept. Defaults to None.
            parse_mode (str | None, optional): Mode for parsing entities in the new caption. Defaults to None.
            caption_entities (list[MessageEntity] | None, optional): A JSON-serialized list of special entities that appear in the new caption, which can be specified instead of parse_mode. Defaults to None.
            disable_notification (bool | None, optional): Sends the message silently. Users will receive a notification with no sound. Defaults to None.
            protect_content (bool | None, optional): Protects the contents of the sent message from forwarding and saving. Defaults to None.
            reply_to_message_id (bool | None, optional): If the message is a reply, ID of the original message. Defaults to None.
            allow_sending_without_reply (bool | None, optional): Pass True if the message should be sent even if the specified replied-to message is not found. Defaults to None.
            reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply, optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user. Defaults to None.
        """
        pass

    def send_photo(self, chat_id: int | str, photo: InputFile | str, message_thread_id: int | None = None,
                   caption: str | None = None, parse_mode: str | None = None, caption_entities: list[MessageEntity]
                   | None = None, disable_notification: bool | None = None, protect_content: bool | None = None,
                   reply_to_message_id: bool | None = None, allow_sending_without_reply: bool | None = None,
                   reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply | None = None):
        """Use this method to send photos. On success, the sent Message is returned.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
            photo (InputFile | str): Photo to send. Pass a file_id as String to send a photo that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a photo from the Internet, or upload a new photo using multipart/form-data. The photo must be at most 10 MB in size. The photo's width and height must not exceed 10000 in total. Width and height ratio must be at most 20.
            message_thread_id (int | None, optional): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only. Defaults to None.
            caption (str | None, optional): Photo caption (may also be used when resending photos by file_id), 0-1024 characters after entities parsing. Defaults to None.
            parse_mode (str | None, optional): Mode for parsing entities in the photo caption. Defaults to None.
            caption_entities (list[MessageEntity] | None, optional): A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode. Defaults to None.
            disable_notification (bool | None, optional): Sends the message silently. Users will receive a notification with no sound. Defaults to None.
            protect_content (bool | None, optional): Protects the contents of the sent message from forwarding and saving. Defaults to None.
            reply_to_message_id (bool | None, optional): If the message is a reply, ID of the original message. Defaults to None.
            allow_sending_without_reply (bool | None, optional): Pass True if the message should be sent even if the specified replied-to message is not found. Defaults to None.
            reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply, optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user. Defaults to None.
        """
        pass

    def send_audio(self, chat_id: int | str, photo: InputFile | str, message_thread_id: int | None = None,
                   caption: str | None = None, parse_mode: str | None = None, caption_entities: list[MessageEntity]
                   | None = None, duration: int | None = None, performer: str | None = None, title: str | None = None,
                   thumb: InputFile | str | None = None, disable_notification: bool | None = None,
                   protect_content: bool | None = None, reply_to_message_id: bool | None = None,
                   allow_sending_without_reply: bool | None = None,
                   reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply | None = None):
        """Use this method to send audio files, if you want Telegram clients to display them in the music player. Your audio must be in the .MP3 or .M4A format. On success, the sent Message is returned. Bots can currently send audio files of up to 50 MB in size, this limit may be changed in the future.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
            photo (InputFile | str): Photo to send. Pass a file_id as String to send a photo that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a photo from the Internet, or upload a new photo using multipart/form-data. The photo must be at most 10 MB in size. The photo's width and height must not exceed 10000 in total. Width and height ratio must be at most 20.
            message_thread_id (int | None, optional): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only. Defaults to None.
            caption (str | None, optional): Audio caption, 0-1024 characters after entities parsing. Defaults to None.
            parse_mode (str | None, optional): Mode for parsing entities in the audio caption. Defaults to None.
            caption_entities (list[MessageEntity] | None, optional): A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode. Defaults to None.
            duration (int | None, optional): Duration of the audio in seconds. Defaults to None.
            performer (str | None, optional): Performer. Defaults to None
            title (str | None, optional): Track name. Defaults None.
            thumb (InputFile | str | None, optional): Thumbnail of the file sent. Defaults to None.
            disable_notification (bool | None, optional): Sends the message silently. Users will receive a notification with no sound. Defaults to None.
            protect_content (bool | None, optional): Protects the contents of the sent message from forwarding and saving. Defaults to None.
            reply_to_message_id (bool | None, optional): If the message is a reply, ID of the original message. Defaults to None.
            allow_sending_without_reply (bool | None, optional): Pass True if the message should be sent even if the specified replied-to message is not found. Defaults to None.
            reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply, optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user. Defaults to None.
        """
        pass

    def send_document(self, chat_id: int | str, document: InputFile | str, message_thread_id: int | None = None,
                      caption: str | None = None,  parse_mode: str | None = None, caption_entities: list[MessageEntity]
                      | None = None, disable_content_type_detection: bool | None = None,
                      thumb: InputFile | str | None = None, disable_notification: bool | None = None,
                      protect_content: bool | None = None, reply_to_message_id: bool | None = None,
                      allow_sending_without_reply: bool | None = None,
                      reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply | None = None):
        """Use this method to send general files. On success, the sent Message is returned. Bots can currently send files of any type of up to 50 MB in size, this limit may be changed in the future.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
            document (InputFile | str): File to send. Pass a file_id as String to send a photo that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a photo from the Internet, or upload a new photo using multipart/form-data. The photo must be at most 10 MB in size. The photo's width and height must not exceed 10000 in total. Width and height ratio must be at most 20.
            message_thread_id (int | None, optional): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only. Defaults to None.
            caption (str | None, optional): Document caption(may also be used when resending documents by file_id), 0-1024 characters after entities parsing. Defaults to None.
            parse_mode (str | None, optional): Mode for parsing entities in the audio caption. Defaults to None.
            caption_entities (list[MessageEntity] | None, optional): A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode. Defaults to None.
            disable_content_type_detection (bool | None, optional): Disables automatic server-side content type detection for files uploaded using multipart/form-data. Deafults to None.
            thumb (InputFile | str | None, optional): Thumbnail of the file sent. Defaults to None.
            disable_notification (bool | None, optional): Sends the message silently. Users will receive a notification with no sound. Defaults to None.
            protect_content (bool | None, optional): Protects the contents of the sent message from forwarding and saving. Defaults to None.
            reply_to_message_id (bool | None, optional): If the message is a reply, ID of the original message. Defaults to None.
            allow_sending_without_reply (bool | None, optional): Pass True if the message should be sent even if the specified replied-to message is not found. Defaults to None.
            reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply, optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user. Defaults to None.
        """
        pass

    def send_video(self, chat_id: int | str, video: InputFile | str, message_thread_id: str | None = None,
                   duration: int | None = None, width: int | None = None, height: int | None = None,
                   thumb: InputFile | str | None = None, caption: str | None = None, parse_mode: str | None = None,
                   caption_entities: list[MessageEntity] | None = None, supports_streaming: bool | None = None,
                   disable_notification: bool | None = None, protect_content: bool | None = None,
                   reply_to_message_id: int | None = None, allow_sending_without_reply: bool | None = None,
                   reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply | None = None):
        """Use this method to send video files, Telegram clients support MPEG4 videos (other formats may be sent as Document). On success, the sent Message is returned. Bots can currently send video files of up to 50 MB in size, this limit may be changed in the future.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
            video (InputFile | str): Video to send. Pass a file_id as String to send a video that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a video from the Internet, or upload a new video using multipart/form-data
            message_thread_id (str | None, optional): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only. Defaults to None.
            duration (int | None, optional): Duration of sent video in seconds. Defaults to None.
            width (int | None, optional): Video width. Defaults to None.
            height (int | None, optional): Video height. Defaults to None.
            thumb (InputFile | str | None, optional): Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. Defaults to None.
            caption (str | None, optional): Video caption (may also be used when resending videos by file_id), 0-1024 characters after entities parsing. Defaults to None.
            parse_mode (str | None, optional): Mode for parsing entities in the video caption. Defaults to None.
            caption_entities (list[MessageEntity] | None, optional): A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode. Defaults to None.
            supports_streaming (bool | None, optional): Pass True if the uploaded video is suitable for streaming. Defaults to None.
            disable_notification (bool | None, optional): Sends the message silently. Users will receive a notification with no sound. Defaults to None.
            protect_content (bool | None, optional): Protects the contents of the sent message from forwarding and saving. Defaults to None.
            reply_to_message_id (int | None, optional): If the message is a reply, ID of the original message. Defaults to None.
            allow_sending_without_reply (bool | None, optional): Pass True if the message should be sent even if the specified replied-to message is not found. Defaults to None.
            reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply, optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user. Defaults to None.
        """
        pass

    def send_animation(self, chat_id: int | str, animation: InputFile | str, message_thread_id: str | None = None,
                       duration: int | None = None, width: int | None = None, height: int | None = None,
                       thumb: InputFile | str | None = None, caption: str | None = None, parse_mode: str | None = None,
                       caption_entities: list[MessageEntity] | None = None, supports_streaming: bool | None = None,
                       disable_notification: bool | None = None, protect_content: bool | None = None,
                       reply_to_message_id: int | None = None, allow_sending_without_reply: bool | None = None,
                       reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply | None = None):
        """Use this method to send animation files (GIF or H.264/MPEG-4 AVC video without sound). On success, the sent Message is returned. Bots can currently send animation files of up to 50 MB in size, this limit may be changed in the future.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
            animation (InputFile | str): Animation to send. Pass a file_id as String to send a video that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a video from the Internet, or upload a new video using multipart/form-data
            message_thread_id (str | None, optional): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only. Defaults to None.
            duration (int | None, optional): Duration of sent animation in seconds. Defaults to None.
            width (int | None, optional): Animation width. Defaults to None.
            height (int | None, optional): Animation height. Defaults to None.
            thumb (InputFile | str | None, optional): Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. Defaults to None.
            caption (str | None, optional): Animation caption (may also be used when resending videos by file_id), 0-1024 characters after entities parsing. Defaults to None.
            parse_mode (str | None, optional): Mode for parsing entities in the video caption. Defaults to None.
            caption_entities (list[MessageEntity] | None, optional): A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode. Defaults to None.
            supports_streaming (bool | None, optional): Pass True if the uploaded video is suitable for streaming. Defaults to None.
            disable_notification (bool | None, optional): Sends the message silently. Users will receive a notification with no sound. Defaults to None.
            protect_content (bool | None, optional): Protects the contents of the sent message from forwarding and saving. Defaults to None.
            reply_to_message_id (int | None, optional): If the message is a reply, ID of the original message. Defaults to None.
            allow_sending_without_reply (bool | None, optional): Pass True if the message should be sent even if the specified replied-to message is not found. Defaults to None.
            reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply, optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user. Defaults to None.
        """
        pass

    def send_voice(self, chat_id: int | str, voice: InputFile | str, message_thread_id: str | None = None,
                   duration: int | None = None, caption: str | None = None, parse_mode: str | None = None,
                   caption_entities: list[MessageEntity] | None = None, disable_notification: bool | None = None,
                   protect_content: bool | None = None, reply_to_message_id: int | None = None,
                   allow_sending_without_reply: bool | None = None,
                   reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply | None = None):
        """Use this method to send audio files, if you want Telegram clients to display the file as a playable voice message. For this to work, your audio must be in an .OGG file encoded with OPUS (other formats may be sent as Audio or Document). On success, the sent Message is returned. Bots can currently send voice messages of up to 50 MB in size, this limit may be changed in the future.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
            voice (InputFile | str): Audio file to send. Pass a file_id as String to send a video that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a video from the Internet, or upload a new video using multipart/form-data
            message_thread_id (str | None, optional): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only. Defaults to None.
            duration (int | None, optional): Duration of sent video in seconds. Defaults to None.
            caption (str | None, optional): Video caption (may also be used when resending videos by file_id), 0-1024 characters after entities parsing. Defaults to None.
            parse_mode (str | None, optional): Mode for parsing entities in the video caption. Defaults to None.
            caption_entities (list[MessageEntity] | None, optional): A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode. Defaults to None.
            disable_notification (bool | None, optional): Sends the message silently. Users will receive a notification with no sound. Defaults to None.
            protect_content (bool | None, optional): Protects the contents of the sent message from forwarding and saving. Defaults to None.
            reply_to_message_id (int | None, optional): If the message is a reply, ID of the original message. Defaults to None.
            allow_sending_without_reply (bool | None, optional): Pass True if the message should be sent even if the specified replied-to message is not found. Defaults to None.
            reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply, optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user. Defaults to None.
        """
        pass

    def send_video_note(self, chat_id: int | str, video_note: InputFile | str, message_thread_id: str | None = None,
                        duration: int | None = None, height: int | None = None,
                        thumb: InputFile | str | None = None, caption: str | None = None, parse_mode: str | None = None,
                        caption_entities: list[MessageEntity] | None = None, supports_streaming: bool | None = None,
                        disable_notification: bool | None = None, protect_content: bool | None = None,
                        reply_to_message_id: int | None = None, allow_sending_without_reply: bool | None = None,
                        reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply | None = None):
        """As of v.4.0, Telegram clients support rounded square MPEG4 videos of up to 1 minute long. Use this method to send video messages. On success, the sent Message is returned.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
            video_note (InputFile | str): Video to send. Pass a file_id as String to send a video that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a video from the Internet, or upload a new video using multipart/form-data
            message_thread_id (str | None, optional): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only. Defaults to None.
            duration (int | None, optional): Duration of sent video in seconds. Defaults to None.
            height (int | None, optional): Video height. Defaults to None.
            thumb (InputFile | str | None, optional): Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. Defaults to None.
            caption (str | None, optional): Video caption (may also be used when resending videos by file_id), 0-1024 characters after entities parsing. Defaults to None.
            parse_mode (str | None, optional): Mode for parsing entities in the video caption. Defaults to None.
            caption_entities (list[MessageEntity] | None, optional): A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode. Defaults to None.
            disable_notification (bool | None, optional): Sends the message silently. Users will receive a notification with no sound. Defaults to None.
            protect_content (bool | None, optional): Protects the contents of the sent message from forwarding and saving. Defaults to None.
            reply_to_message_id (int | None, optional): If the message is a reply, ID of the original message. Defaults to None.
            allow_sending_without_reply (bool | None, optional): Pass True if the message should be sent even if the specified replied-to message is not found. Defaults to None.
            reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply, optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user. Defaults to None.
        """
        pass

    def send_media_group(self, chat_id: int | str, media: list[InputMediaAudio | InputMediaDocument | InputMediaPhoto | InputMediaVideo],
                         message_thread_id: str | None = None, disable_notification: bool | None = None,
                         protect_content: bool | None = None, reply_to_message_id: int | None = None,
                         allow_sending_without_reply: bool | None = None):
        """Use this method to send a group of photos, videos, documents or audios as an album. Documents and audio files can be only grouped in an album with messages of the same type. On success, an array of Messages that were sent is returned.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
            media (list[InputMediaAudio | InputMediaDocument | InputMediaPhoto | InputMediaVideo]): A JSON-serialized array describing messages to be sent, must include 2-10 items.
            message_thread_id (str | None, optional): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only. Defaults to None.
            disable_notification (bool | None, optional): Sends the message silently. Users will receive a notification with no sound. Defaults to None.
            protect_content (bool | None, optional): Protects the contents of the sent message from forwarding and saving. Defaults to None.
            reply_to_message_id (int | None, optional): If the message is a reply, ID of the original message. Defaults to None.
            allow_sending_without_reply (bool | None, optional): Pass True if the message should be sent even if the specified replied-to message is not found. Defaults to None.
        """
        pass

    def send_location(self, chat_id: int | str, latitude: float, longitude: float, message_thread_id: int | None = None,
                      horizontal_accuracy: float | None = None, live_period: int | None = None, heading: int | None = None,
                      proximity_alert_radius: int | None = None, disable_notification: bool | None = None,
                      protect_content: bool | None = None, reply_to_message_id: int | None = None,
                      allow_sending_without_reply: bool | None = None,
                      reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply | None = None):
        """Use this method to send point on the map. On success, the sent Message is returned.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername).
            latitude (float): Latitude of the location
            longitude (float): Longitude of the location
            message_thread_id (int | None, optional): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only. Defaults to None.
            horizontal_accuracy (float | None, optional): The radius of uncertainty for the location, measured in meters; 0-1500. Defaults to None.
            live_period (int | None, optional): Period in seconds for which the location will be updated (see Live Locations, should be between 60 and 86400. Defaults to None.
            heading (int | None, optional): For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified. Defaults to None.
            proximity_alert_radius (int | None, optional): For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified. Defaults to None.
            disable_notification (bool | None, optional): Sends the message silently. Users will receive a notification with no sound. Defaults to None.
            protect_content (bool | None, optional): Protects the contents of the sent message from forwarding and saving. Defaults to None.
            reply_to_message_id (int | None, optional): If the message is a reply, ID of the original message. Defaults to None.
            allow_sending_without_reply (bool | None, optional): Pass True if the message should be sent even if the specified replied-to message is not found. Defaults to None.
            reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply, optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user. Defaults to None.
        """
        pass

    def edit_message_live_location(self, chat_id: int | str, latitude: float, longitude: float, message_id: int | None = None,
                                   inline_message_id: str | None = None, horizontal_accuracy: float | None = None,
                                   heading: int | None = None, proximity_alert_radius: int | None = None,
                                   reply_markup: InlineKeyboardMarkup | None = None):
        """Use this method to edit live location messages. A location can be edited until its live_period expires or editing is explicitly disabled by a call to stopMessageLiveLocation. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername).
            latitude (float): Latitude of the new location
            longitude (float): Longitude of the new location
            message_id (int | None, optional): Required if inline_message_id is not specified. Identifier of the message to edit. Defaults to None.
            inline_message_id (str | None, optional): Required if chat_id and message_id are not specified. Identifier of the inline message.
            horizontal_accuracy (float | None, optional): The radius of uncertainty for the location, measured in meters; 0-1500. Defaults to None.
            heading (int | None, optional): For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified. Defaults to None.
            proximity_alert_radius (int | None, optional): The maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified. Defaults to None.
            reply_markup (InlineKeyboardMarkup, optional): A JSON-serialized object for a new inline keyboard. Defaults to None.
        """
        pass

    def stop_message_live_location(self, chat_id: int | None = None, message_id: int | None = None, inline_message_id: int | None = None,
                                   reply_markup: InlineKeyboardMarkup | None = None):
        """Use this method to stop updating a live location message before live_period expires. On success, if the message is not an inline message, the edited Message is returned, otherwise True is returned.

        Args:
            chat_id (int | None, optional): Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername)
            message_id (int | None, optional): Required if inline_message_id is not specified. Identifier of the message with live location to stop. Defaults to None.
            inline_message_id (int | None, optional): Required if chat_id and message_id are not specified. Identifier of the inline message. Defaults to None.
            reply_markup (InlineKeyboardMarkup | None, optional): A JSON-serialized object for a new inline keyboard. Defaults to None.
        """
        pass

    def send_venue(self, chat_id: int, latitude: float, longitude: float, title: str, address: str,
                   message_thread_id: int | None = None, foursquare_id: str | None = None, foursquare_type: str | None = None,
                   google_place_id: str | None = None, google_place_type: str | None = None,
                   disable_notification: bool | None = None, protect_content: bool | None = None,
                   reply_to_message_id: int | None = None, allow_sending_without_reply: bool | None = None,
                   reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply | None = None):
        """Use this method to send information about a venue. On success, the sent Message is returned.

        Args:
            chat_id (int): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
            latitude (float): Latitude of the venue
            longitude (float): Longitude of the venue
            title (str): Name of the venue
            address (str): Address of the venue
            message_thread_id (int | None, optional): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.
            foursquare_id (str | None, optional): Foursquare identifier of the venue. Defaults to None.
            foursquare_type (str | None, optional): Foursquare type of the venue, if known. (For example, “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.). Defaults to None.
            google_place_id (str | None, optional): Google Places identifier of the venue. Defaults to None.
            google_place_type (str | None, optional): Google Places type of the venue. Defaults to None.
            disable_notification (bool | None, optional): Sends the message silently. Users will receive a notification with no sound. Defaults to None.
            protect_content (bool | None, optional): Protects the contents of the sent message from forwarding and saving. Defaults to None.
            reply_to_message_id (int | None, optional): If the message is a reply, ID of the original message. Defaults to None.
            allow_sending_without_reply (bool | None, optional): Pass True if the message should be sent even if the specified replied-to message is not found. Defaults to None.
            reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply | None, optional): _description_. Defaults to None.
        """
        pass

    def send_contact(self, chat_id: int, phone_number: int, first_name: str, last_name: str | None = None,
                     message_thread_id: int | None = None, vcard: str | None = None, disable_notification: bool | None = None,
                     protect_content: bool | None = None, reply_to_messge_id: bool | None = None,
                     allow_sending_without_reply: bool | None = None,
                     reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply | None = None):
        """Use this method to send phone contacts. On success, the sent Message is returned.

        Args:
            chat_id (int): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
            phone_number (int): Contact's phone number
            first_name (str): Contact's first name
            last_name (str | None, optional): Contact's last name. Defaults to None.
            message_thread_id (int | None, optional): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only. Defaults to None.
            vcard (str | None, optional): Additional data about the contact in the form of a vCard, 0-2048 bytes. Defaults to None.
            disable_notification (bool | None, optional): Sends the message silently. Users will receive a notification with no sound. Defaults to None.
            protect_content (bool | None, optional): Protects the contents of the sent message from forwarding and saving. Defaults to None.
            reply_to_messge_id (bool | None, optional): If the message is a reply, ID of the original message. Defaults to None.
            allow_sending_without_reply (bool | None, optional): Pass True if the message should be sent even if the specified replied-to message is not found. Defaults to None.
            reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply | None, optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user. Defaults to None.
        """
        pass

    def send_poll(self, chat_id: int, question: str, options: list[str], message_thread_id: int | None = None,
                  is_anonymous: bool | None = None, type: str = "regular", allows_multiple_answers: bool | None = None,
                  correct_option_id: int | None = None, explanation: str | None = None, explanation_parse_mode: str | None = None,
                  explanation_entities: list[MessageEntity] | None = None, open_period: int | None = None, close_date: int | None = None,
                  is_closed: bool | None = None, disable_notification: bool | None = None, protect_content: bool | None = None,
                  reply_to_message_id: bool | None = None, allow_sending_without_reply: bool | None = None,
                  reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply | None = None):
        """Use this method to send a native poll. On success, the sent Message is returned.

        Args:
            chat_id (int): Unique identifier for the target chat or username of the target channel (in the format @channelusername).
            question (str): Poll question, 1-300 characters
            options (list[str]): A JSON-serialized list of answer options, 2-10 strings 1-100 characters each.
            message_thread_id (int | None, optional): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only. Defaults to None.
            is_anonymous (bool | None, optional): True, if the poll needs to be anonymous, defaults to True. Defaults to None.
            type (str | None, optional): Poll type, “quiz” or “regular”. Defaults to “regular”.
            allows_multiple_answers (bool | None, optional): True, if the poll allows multiple answers, ignored for polls in quiz mode, defaults to False. Defaults to None.
            correct_option_id (int | None, optional): 0-based identifier of the correct answer option, required for polls in quiz mode. Defaults to None.
            explanation (str | None, optional): Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters with at most 2 line feeds after entities parsing. Defaults to None.
            explanation_parse_mode (str | None, optional): Mode for parsing entities in the explanation. Defaults to None.
            explanation_entities (list[MessageEntity] | None, optional): A JSON-serialized list of special entities that appear in the poll explanation, which can be specified instead of parse_mode. Defaults to None.
            open_period (int | None, optional): Amount of time in seconds the poll will be active after creation, 5-600. Can't be used together with close_date. Defaults to None.
            close_date (int | None, optional): Point in time (Unix timestamp) when the poll will be automatically closed. Must be at least 5 and no more than 600 seconds in the future. Can't be used together with open_period. Defaults to None.
            is_closed (bool | None, optional): Pass True if the poll needs to be immediately closed. This can be useful for poll preview.. Defaults to None.
            disable_notification (bool | None, optional): Sends the message silently. Users will receive a notification with no sound. Defaults to None.
            protect_content (bool | None, optional): Protects the contents of the sent message from forwarding and saving. Defaults to None.
            reply_to_message_id (bool | None, optional): If the message is a reply, ID of the original message. Defaults to None.
            allow_sending_without_reply (bool | None, optional): Pass True if the message should be sent even if the specified replied-to message is not found. Defaults to None.
            reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply | None, optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user. Defaults to None.
        """
        pass

    def send_dice(self, chat_id: int, message_thread_id: int | None = None, emoji: str | None = None, disable_notification: bool | None = None,
                  protect_content: bool | None = None, reply_to_message_id: int | None = None, allow_sending_without_reply: bool | None = None,
                  reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply | None = None):
        """Use this method to send an animated emoji that will display a random value. On success, the sent Message is returned.

        Args:
            chat_id (int): Unique identifier for the target chat or username of the target channel (in the format @channelusername).
            message_thread_id (int | None, optional): Unique identifier for the target message thread (topic) of the forum; for forum supergroups only. Defaults to None.
            emoji (str | None, optional): Emoji on which the dice throw animation is based. Currently, must be one of “🎲”, “🎯”, “🏀”, “⚽”, “🎳”, or “🎰”. Dice can have values 1-6 for “🎲”, “🎯” and “🎳”, values 1-5 for “🏀” and “⚽”, and values 1-64 for “🎰”. Defaults to “🎲”. Defaults to None.
            disable_notification (bool | None, optional): Sends the message silently. Users will receive a notification with no sound. Defaults to None.
            protect_content (bool | None, optional): Protects the contents of the sent message from forwarding. Defaults to None.
            reply_to_message_id (int | None, optional): If the message is a reply, ID of the original message. Defaults to None.
            allow_sending_without_reply (bool | None, optional): Pass True if the message should be sent even if the specified replied-to message is not found. Defaults to None.
            reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply | None, optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user. Defaults to None.
        """
        pass

    def send_chat_action(self, chat_id: int, action: str):
        """Use this method when you need to tell the user that something is happening on the bot's side. The status is set for 5 seconds or less (when a message arrives from your bot, Telegram clients clear its typing status). Returns True on success.

        Args:
            chat_id (int): Unique identifier for the target chat or username of the target channel (in the format @channelusername).
            action (str): Type of action to broadcast. Choose one, depending on what the user is about to receive: typing for text messages, upload_photo for photos, record_video or upload_video for videos, record_voice or upload_voice for voice notes, upload_document for general files, choose_sticker for stickers, find_location for location data, record_video_note or upload_video_note for video notes.
        """
        pass

    def get_user_profile_photos(self, user_id: int, offset: int | None = None, limit: int | None = None):
        """Use this method to get a list of profile pictures for a user. Returns a UserProfilePhotos object.

        Args:
            user_id (int): Unique identifier of the target user.
            offset (int | None, optional): Sequential number of the first photo to be returned. By default, all photos are returned. Defaults to None.
            limit (int | None, optional): Limits the number of photos to be retrieved. Values between 1-100 are accepted. Defaults to 100. Defaults to None.
        """
        pass

    def get_file(self, file_id: int) -> None:
        """Use this method to get basic information about a file and prepare it for downloading.

        Args:
            file_id (int): File identifier to get information about.
        """
        pass

    def ban_chat_member(self, chat_id: int | str, user_id: int, until_date: str | None = None, revoke_messages: bool | None = None) -> bool:
        """Use this method to ban a user in a group, a supergroup or a channel. In the case of supergroups and channels, the user will not be able to return to the chat on their own using invite links, etc., unless unbanned first. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights.

        Args:
            chat_id (int): Unique identifier for the target group or username of the target supergroup or channel (in the format @channelusername)
            user_id (int): Unique identifier of the target user.
            until_date (str | None, optional): Date when the user will be unbanned, unix time. If user is banned for more than 366 days or less than 30 seconds from the current time they are considered to be banned forever. Applied for supergroups and channels only. Defaults to None.
            revoke_messages (bool | None, optional): Pass True to delete all messages from the chat for the user that is being removed. If False, the user will be able to see messages in the group that were sent before the user was removed. Always True for supergroups and channels. Defaults to None.
        Returns:
            bool: Returns True on success.
        """
        return True

    def unban_chat_member(self, chat_id: int | str, user_id: int, only_if_banned: bool | None = None) -> bool:
        """Use this method to unban a previously banned user in a supergroup or channel. The user will not return to the group or channel automatically, but will be able to join via link, etc. The bot must be an administrator for this to work. By default, this method guarantees that after the call the user is not a member of the chat, but will be able to join it. So if the user is a member of the chat they will also be removed from the chat. If you don't want this, use the parameter only_if_banned.

        Args:
            chat_id (int | str): Unique identifier for the target group or username of the target supergroup or channel (in the format @channelusername).
            user_id (int): Unique identifier of the target user.
            only_if_banned (bool | None, optional): Do nothing if the user is not banned. Defaults to None.

        Returns:
            bool: Returns True on success.
        """
        return True

    def restrict_chat_member(self, chat_id: int | str, user_id: int, permissions: ChatPermissions, until_date: str | None = None) -> bool:
        """Use this method to restrict a user in a supergroup. The bot must be an administrator in the supergroup for this to work and must have the appropriate administrator rights. Pass True for all permissions to lift restrictions from a user.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).
            user_id (int): Unique identifier of the target user.
            permissions (ChatPermissions): A JSON-serialized object for new user permissions.
            until_date (str | None, optional): Date when restrictions will be lifted for the user, unix time. If user is restricted for more than 366 days or less than 30 seconds from the current time, they are considered to be restricted forever. Defaults to None.

        Returns:
            bool: Returns True on success.
        """
        pass

    def promote_chat_member(self, chat_id: int, user_id: int, is_anonymous: bool | None = None,
                            can_manage_chat: bool | None = None, can_post_messages: bool | None = None,
                            can_edit_messages: bool | None = None, can_delete_messages: bool | None = None,
                            can_manage_video_chats: bool | None = None, can_restrict_members: bool | None = None,
                            can_promote_members: bool | None = None, can_change_info: bool | None = None,
                            can_invite_users: bool | None = None, can_pin_messages: bool | None = None,
                            can_manage_topics: bool | None = None) -> bool:
        """Use this method to promote or demote a user in a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Pass False for all boolean parameters to demote a user.

        Args:
            chat_id (int): Unique identifier for the target chat or username of the target channel (in the format @channelusername).
            user_id (int): Unique identifier of the target user
            is_anonymous (bool | None, optional): Pass True if the administrator's presence in the chat is hidden. Defaults to None.
            can_manage_chat (bool | None, optional): Pass True if the administrator can access the chat event log, chat statistics, message statistics in channels, see channel members, see anonymous administrators in supergroups and ignore slow mode. Implied by any other administrator privilege. Defaults to None.
            can_post_messages (bool | None, optional): Pass True if the administrator can create channel posts, channels only. Defaults to None.
            can_edit_messages (bool | None, optional): Pass True if the administrator can edit messages of other users and can pin messages, channels only. Defaults to None.
            can_delete_messages (bool | None, optional): Pass True if the administrator can delete messages of other users. Defaults to None.
            can_manage_video_chats (bool | None, optional): Pass True if the administrator can manage video chats. Defaults to None.
            can_restrict_members (bool | None, optional): Pass True if the administrator can restrict, ban or unban chat members. Defaults to None.
            can_promote_members (bool | None, optional): Pass True if the administrator can add new administrators with a subset of their own privileges or demote administrators that he has promoted, directly or indirectly (promoted by administrators that were appointed by him). Defaults to None.
            can_change_info (bool | None, optional): Pass True if the administrator can change chat title, photo and other settings. Defaults to None.
            can_invite_users (bool | None, optional): Pass True if the administrator can invite new users to the chat. Defaults to None.
            can_pin_messages (bool | None, optional): Pass True if the administrator can pin messages, supergroups only. Defaults to None.
            can_manage_topics (bool | None, optional): Pass True if the user is allowed to create, rename, close, and reopen forum topics, supergroups only. Defaults to None.

        Returns:
            bool: Returns True on success.
        """
        pass

    def setChatAdministratorCustomTitle(self, chat_id: int | str, user_id: int, custom_title: str) -> bool:
        """Use this method to set a custom title for an administrator in a supergroup promoted by the bot.

        Args:
            chat_id (int | str): Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).
            user_id (int): Unique identifier of the target user
            custom_title (str): New custom title for the administrator; 0-16 characters, emoji are not allowed.

        Returns:
            bool: Returns True on success.
        """
        return True
