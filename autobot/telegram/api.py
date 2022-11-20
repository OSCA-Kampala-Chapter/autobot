"""
This module contains a class having methods representing the bot api methods
"""

from autobot.telegram.objects.message import MessageEntity


class BotAPI:

    def get_me(self):
        pass

    def logout(self):
        pass

    def close(self):
        pass

    def send_message(self, chat_id: int | str, text: str, message_thread_id: int | None = None,
                     parse_mode: str | None = None, entities: list[MessageEntity] | None = None,
                     disable_web_page_preview: bool | None = None, disable_notification: bool | None = None,
                     protect_content: bool | None = None, reply_to_message_id: int | None = None,
                     allow_sending_without_reply: bool | None = None, reply_markup=None):
        pass

    def foward_message(self, chat_id: int | str, from_chat_id: int | str, message_id: int,
                       message_thread_id: int | None = None, disable_notification: bool | None = None,
                       protect_content: int | None = None):
        pass

    def copy_message(self, chat_id: int | str, from_chat_id: int | str, message_id: int | str,
                     message_thread_id: int | None = None, caption: str | None = None, parse_mode: str | None = None,
                     caption_entities: list[MessageEntity] | None = None, disable_notification: bool | None = None,
                     protect_content: bool | None = None, reply_to_message_id: bool | None = None,
                     allow_sending_without_reply: bool | None = None, reply_markup=None):
        pass
