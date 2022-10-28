from .base import BaseObject

class User(BaseObject):
    def __init__ (self,
        id,
        is_bot,
        first_name,
        last_name = None,
        username = None,
        language_code = None,
        is_premium = None,
        added_to_attachment_menu = None,
        can_join_groups = None,
        can_read_all_group_messages = None,
        supports_inline_queries = None
    ):
        self.id = id
        self.is_bot = is_bot
        self.first_name = first_name
        self.username = username
        self.language_code = language_code
        self.is_premium = is_premium
        self.added_to_attachment_menu = added_to_attachment_menu
        self.can_join_groups = can_join_groups
        self.can_read_all_group_messages = can_read_all_group_messages
        self.supports_inline_queries = supports_inline_queries

class UserProfilePhotos(BaseObject):
    def __init__ (self,
        total_count,
        photos,
    ):
        self.total_count = total_count
        self.photos = photos
