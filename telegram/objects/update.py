from .base import BaseObject

class Update (BaseObject):
    def __init__ (self,
        update_id,
        message = None,
        edited_message = None,
        channel_post = None,
        edited_channel_post = None,
        inline_query = None,
        chosen_inline_result = None,
        callback_query = None,
        shipping_query = None,
        pre_checkout_query = None,
        poll = None,
        poll_answer = None,
        my_chat_member = None,
        chat_member = None,
        chat_join_request = None,
    ):
        self.update_id = update_id
        self.message = message
        self.edited_message = edited_message
        self.channel_post = channel_post
        self.edited_channel_post = edited_channel_post
        self.inline_query = inline_query
        self.chosen_inline_result = chosen_inline_result
        self.callback_query = callback_query
        self.shipping_query = shipping_query
        self.pre_checkout_query = pre_checkout_query
        self.poll = poll
        self.poll_answer = poll_answer
        self.my_chat_member = my_chat_member
        self.chat_member = chat_member
        self.chat_join_request = chat_join_request