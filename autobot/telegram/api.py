"""
This module contains a class having methods representing the bot api methods
"""

from autobot.telegram.objects.message import MessageEntity


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
                     allow_sending_without_reply: bool | None = None, reply_markup=None):
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
                     allow_sending_without_reply: bool | None = None, reply_markup=None):
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
