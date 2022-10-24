class Message:
    def __init__ (self,
        message_id,
        from_ = None,
        sender_chat = None,
        date = None,
        chat = None,
        forward_from = None
        forward_from_chat = None,
        forward_from_message_id = None,
        forward_signature = None,
        forward_sender_name = None,
        forward_date = None,
        is_automatic_forward = None,
        reply_to_message = None,
        via_bot = None,
        edit_date = None,
        has_protected_content = None,
        media_group_id = None,
        author_signature = None,
        text = None,
        entities = None,
        animation = None,
        audio = None,
        document = None,
        photo = None,
        sticker = None,
        video = None,
        video_note = None,
        voice = None,
        caption = None,
        caption_entities = None,
        contact = None,
        dice = None,
        game = None,
        poll = None,
        venue = None,
        location = None,
        new_chat_members = None,
        left_chat_member = None,
        new_chat_title = None,
        new_chat_photo = None,
        delete_chat_photo = None,
        group_chat_created = None,
        supergroup_chat_created = None,
        channel_chat_created = None,
        message_auto_delete_timer_changed = None,
        migrate_to_chat_id = None,
        migrate_from_chat_id = None,
        pinned_message = None,
        invoice = None,
        successful_payment = None,
        connected_website = None,
        passport_data = None,
        proximity_alert_triggered = None,
        video_chat_scheduled = None,
        video_chat_started = None,
        video_chat_ended = None,
        video_chat_participants_invited = None,
        web_app_data = None,
        reply_markup = None,
    ):
        self.message_id = message_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.forward_from = forward_from
        self.forward_from_chat = forward_from_chat
        self.forward_from_message_id = forward_from_message_id
        self.forward_signature = forward_signature
        self.forward_sender_name = forward_sender_name
        self.forward_date = forward_date
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.text = text
        self.entities = entities
        self.animation = animation
        self.audio = audio
        self.document = document
        self.photo = photo
        self.sticker = sticker
        self.video = video
        self.video_note = video_note
        self.voice = voice
        self.caption = caption
        self.caption_entities = caption_entities
        self.contact = contact
        self.dice = dice
        self.game = game
        self.poll = poll
        self.venue = venue
        self.location = location
        self.new_chat_members = new_chat_members
        self.left_chat_member = left_chat_member
        self.new_chat_title = new_chat_title
        self.new_chat_photo = new_chat_photo
        self.delete_chat_photo = delete_chat_photo
        self.group_chat_created = group_chat_created
        self.supergroup_chat_created = supergroup_chat_created
        self.channel_chat_created = channel_chat_created
        self.message_auto_delete_timer_changed = message_auto_delete_timer_changed
        self.migrate_to_chat_id = migrate_to_chat_id
        self.migrate_from_chat_id = migrate_from_chat_id
        self.pinned_message = pinned_message
        self.invoice = invoice
        self.successful_payment = successful_payment
        self.connected_website = connected_website
        self.passport_data = passport_data
        self.proximity_alert_triggered = proximity_alert_triggered
        self.video_chat_scheduled = video_chat_scheduled
        self.video_chat_started = video_chat_started
        self.video_chat_ended = video_chat_ended
        self.video_chat_participants_invited = video_chat_participants_invited
        self.web_app_data = web_app_data
        self.reply_markup = reply_markup

class MessageAutoDeleteTimerChanged:
    pass 

class MessageEntity:
    def __init__ (self,
        type,
        offset,
        length,
        url = None,
        language = None,
        custom_emoji_id = None,
    ):
        self.type = type
        self.offset = offset
        self.length = length
        self.url = url
        self.language = language
        self.custom_emoji_id = custom_emoji_id

class MessageId:
    def __init__ (self,
        message_id
    ):
        self.message_id = message_id
