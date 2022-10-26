class Chat:
    def __init__(self, 
        id = None,
        type = None,
        title = None,
        username = None,
        first_name = None,
        last_name = None,
        photo = None,
        bio = None,
        has_private_forwards = None,
        has_restricted_voice_and_video_messages	= None,
        join_to_send_messages = None,
        join_by_request = None,
        description = None,
        invite_link = None,
        pinned_message = None,
        permissions = None,
        slow_mode_delay = None,
        message_auto_delete_time = None,
        has_protected_content = None,
        sticker_set_name = None,
        can_set_sticker_set = None,
        linked_chat_id = None,
        location = None ):
            self.id = id
            self.type = type
            self.title = title
            self.username = username
            self.first_name = first_name
            self.last_name = last_name
            self.photo = photo
            self.bio = bio
            self.has_private_forwards = has_private_forwards
            self.has_restricted_voice_and_video_messages = has_restricted_voice_and_video_messages
            self.join_to_send_messages = join_to_send_messages
            self.join_by_request = join_by_request
            self.description = description
            self.invite_link = invite_link
            self.pinned_message = pinned_message
            self.permissions = permissions
            self.slow_mode_delay = slow_mode_delay
            self.message_auto_delete_time = message_auto_delete_time
            self.has_protected_content = has_protected_content
            self.sticker_set_name = sticker_set_name
            self.can_set_sticker_set = can_set_sticker_set
            self.linked_chat_id = linked_chat_id
            self.location = location


    
class ChatAdministratorRights:
    pass
    
class ChatInviteLink:
    pass
    
class ChatJoinRequest:
    pass
    
class ChatLocation:
    pass
    
class ChatPermissions:
    pass
    
class ChatPhoto:
    pass