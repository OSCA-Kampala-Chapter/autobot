from autobot.telegram.objects import *
from autobot.telegram.games.objects import *
from autobot.telegram.inline.objects import *
from autobot.telegram.passport.objects import *
from autobot.telegram.payments.objects import *
from autobot.telegram.stickers.objects import *


InlineQueryResults = list[InlineQueryResult, InlineQueryResultArticle, InlineQueryResultAudio, InlineQueryResultCachedAudio, InlineQueryResultCachedDocument, InlineQueryResultCachedGif, InlineQueryResultCachedMpeg4Gif, InlineQueryResultCachedPhoto, InlineQueryResultCachedSticker, InlineQueryResultCachedVideo, InlineQueryResultCachedVoice, InlineQueryResultContact, InlineQueryResultDocument, InlineQueryResultGame, InlineQueryResultGif, InlineQueryResultLocation, InlineQueryResultMpeg4Gif, InlineQueryResultPhoto, InlineQueryResultVenue, InlineQueryResultVideo, InlineQueryResultVoice]

class Parser:
    
    # methods to parse general telegram objects
    
    def _parse_update (self,key:int,val:dict) -> Update:
        update_obj = Update()
        
        for k,v in val.items():
            match k:
            
                case "message"|"edited_message"|"channel_post"|"edited_channel_post":
                    msg = self._parse_message(k,v)
                    setattr(update_obj,k,msg)
                    
                case "inline_query"|"chosen_inline_result":
                    qry = self._parse_inlinekeyboardobjects(k,v)
                    setattr(update_obj,k,qry)
                    
                case "callback_query":
                    cb_qry = self._parse_callbackquery(k,v)
                    setattr(update_obj,k,cb_qry)
                    
                case "shipping_query"|"pre_checkout_query":
                    qry = self._parse_payments(k,v)
                    setattr(update_obj,k,qry)
                    
                case "poll"|"poll_answer":
                    poll = self._parse_poll(k,v)
                    setattr(update_obj,k,poll)
                    
                case "my_chat_member"|"chat_member":
                    ch_mbr = self._parse_chatmember(k,v)
                    setattr(update_obj,k,ch_mbr)
                    
                case "chat_join_request":
                    cjr = self._parse_chat(k,v)
                    setattr(update_obj,k,cjr)
                    
                case _:
                    setattr(update_obj,k,v)

        return update_obj
    
    def _parse_user (self,key,val:dict|list) -> User|UserProfilePhotos:
        user_obj = None
        if (key == "from" or
            key == "forward_from" or
            key == "via_bot" or
            key == "user"
         ):
            user_obj = User()
            for k,v in val.items():
                setattr(user_obj,k,v)

        elif (key == "new_chat_members"):
            user_obj = [self._parse_user("user",user) for user in val]

        return user_obj

    def _parse_chat (self,key,val) -> Chat:
        chat_obj = None
        if (key == "chat" or
            key == "sender_chat" or
            key == "forward_from_chat"
        ):
            chat_obj = Chat()
            for k,v in val.items():
                match k:
                    case "photo":
                        ph = self._parse_chat(k,v)
                        setattr(chat_obj,k,ph)

                    case "pinned_message":
                        msg = self._parse_message(k,v)
                        setattr(chat_obj,k,msg)
                    
                    case "permissions":
                        perms = self._parse_chat(k,v)
                        setattr(chat_obj,k,perms)
                    
                    case "location":
                        loc = self._parse_chat(k,v)
                        setattr(chat_obj,k,loc)
                    
                    case _:
                        setattr(chat_obj,k,v)

        elif (key == "photo"):
            chat_obj = ChatPhoto()
            for k,v in val.items():
                setattr(chat_obj,k,v)

        elif (key == "permissions"):
            chat_obj = ChatPermissions()
            for k,v in val.items():
                setattr(chat_obj,k,v)

        elif (key == "location"):
            chat_obj = ChatLocation()
            for k,v in val.items():
                match k:
                    case "location":
                        loc = self._parse_location(k,v)
                        setattr(chat_obj,loc)
                    case _:
                        setattr(chat_obj,k,v)
        
        return chat_obj

    def _parse_message (self,key:str,val:dict|list) -> Message|MessageEntity|MessageAutoDeleteTimerChanged:
        msg_obj = None

        if (key == "message" or
            key == "reply_to_message" or
            key == "pinned_message"
        ):
            msg_obj = Message()
            for k,v in val.items():
                match k:

                    case "from"|"forward_from"|"via_bot"|"left_chat_member"|"new_chat_members"as frm:
                       usr = self._parse_user(k,v)
                       setattr(msg_obj,"from_",usr) if frm == "from" else setattr(msg_obj,frm,usr)

                    case "chat"|"sender_chat"|"forward_from_chat":
                        ch = self._parse_chat(k,v)
                        setattr(msg_obj,k,ch)

                    case "reply_to_message"|"entities"|"caption_entities"|"message_auto_delete_timer_changed"|"pinned_message":
                        msg = self._parse_message(k,v)
                        setattr(msg_obj,k,msg)

                    case "animation":
                        anim = self._parse_animation(k,v)
                        setattr(msg_obj,k,anim)

                    case "audio":
                        aud = self._parse_audio(k,v)
                        setattr(msg_obj,k,aud)

                    case "document":
                        doc = self._parse_document(k,v)
                        setattr(msg_obj,k,doc)

                    case "photo"|"new_chat_photo":
                        pht = self._parse_photosize(k,v)
                        setattr(msg_obj,k,pht)

                    case "sticker":
                        stkr = self._parse_stickers(k,v)
                        setattr(msg_obj,k,stkr)

                    case "video"|"video_note"|"video_chat_scheduled"|"video_chat_started"|"video_chat_ended"|"video_chat_participants_invited":
                        vid = self._parse_video(k,v)
                        setattr(msg_obj,k,vid)

                    case "voice":
                        voi = self._parse_voice(k,v)
                        setattr(msg_obj,k,voi)

                    case "contact":
                        cont = self._parse_contact(k,v)
                        setattr(msg_obj,k,cont)

                    case "dice":
                        dice = self._parse_dice(k,v)
                        setattr(msg_obj,k,dice)

                    case "poll":
                        poll = self._parse_poll(k,v)
                        setattr(k,poll)

                    case "venue":
                        ven = self._parse_venue(k,v)
                        setattr(msg_obj,k,ven)

                    case "location":
                        loc = self._parse_location(k,v)
                        setattr(msg_obj,k,loc)

                    case "invoice"|"successful_payment":
                        pay_cat = self._parse_payments(k,v) # pay_cat stands for payment category
                        setattr(msg_obj,k,pay_cat)

                    case "passport_data":
                        passport = self._parse_passport(k,v)
                        setattr(msg_obj,k,passport)

                    case "proximity_alert_triggered":
                        pat = self._parse_proximityalerttriggered(k,v)
                        setattr(msg_obj,k,pat)
                    
                    case "forum_topic_created"|"forum_topic_closed"|"forum_topic_reopened":
                        for_top = self._parse_forumtopic(k,v)
                        setattr(msg_obj,k,for_top)

                    case "web_app_data":
                        web_app = self._parse_webapp(k,v)
                        setattr(msg_obj,k,web_app)

                    case "reply_markup":
                        rep = self._parse_inlinekeyboardobjects(k,v)
                        setattr(msg_obj,k,rep)

                    case _ :
                        setattr(msg_obj,k,v)


        elif (
            key == "entities" or
            key == "caption_entities"
            ):
            
            def _entity_parser (entity:dict):
                ent_obj = MessageEntity()
                for k,v in entity.items():
                    if (k == "user"):
                        usr = self._parse_user(k,v)
                        setattr(ent_obj,k,usr)
                    else:
                        setattr(ent_obj,k,v)
                return ent_obj

            msg_obj = [_entity_parser(entity) for entity in val.values()]

        elif (key == "message_auto_delete_timer_changed"):
            msg_obj = MessageAutoDeleteTimerChanged()
            for k,v in val.items():
                setattr(msg_obj,k,v)

        return msg_obj

    # methods to parse games objects
    def _parse_game (self,key:str,val:dict) -> Game|GameHighScore:
        game_obj = None

        if (key == "game"):
            game_obj = Game()
            for k,v in val.items():
                match k:
                    case "photo":
                        pht = self._parse_photosize(k,v)
                        setattr(game_obj,k,pht)
                    case "animation":
                        anim = self._parse_animation(k,v)
                        setattr(game_obj,k,anim)
                    case _:
                        setattr(game_obj,k,v)

        elif (key == "game_high_score"):
            game_obj = GameHighScore()
            for k,v in val.items():
                setattr(game_obj,k,v)

        return game_obj
    
    
    # methods to parse inline objects
    def _parse_inlinequeryresults (self,key:str,val:dict) -> InlineQueryResults:
        inline_obj = None

        if (key == "inline_query_result"):
            inline_obj = InlineQueryResult()
            for k,v in val.items():
                match k:
                    case "photo_url"|"thumb_url"|"gif_url"|"mpeg4_url"|"video_url"|"audio_url"|"voice_url"|"document_url"|"sticker_url"|"photo_file_id"|"gif_file_id"|"mpeg4_file_id"|"video_file_id"|"audio_file_id"|"voice_file_id"|"document_file_id"|"sticker_file_id":
                        setattr(inline_obj,k,v)
                    case "input_message_content":
                        imc = self._parse_inputmessagecontent(k,v)
                        setattr(inline_obj,k,imc)
                    case "reply_markup":
                        rep = self._parse_inlinekeyboardobjects(k,v)
                        setattr(inline_obj,k,rep)
                    case _:
                        setattr(inline_obj,k,v)

    
        elif (key == "inline_query_result_article"):
            inline_obj = InlineQueryResultArticle()
            for k,v in val.items():
                match k:
                    case "input_message_content":
                        imc = self._parse_inputmessagecontent(k,v)
                        setattr(inline_obj,k,imc)
                    case "reply_markup":
                        rep = self._parse_inlinekeyboardobjects(k,v)
                        setattr(inline_obj,k,rep)
                    case _:
                        setattr(inline_obj,k,v)

        elif (key == "inline_query_result_audio"):
            inline_obj = InlineQueryResultAudio()
            for k,v in val.items():
                match k:
                    case "audio_url"|"thumb_url":
                        setattr(inline_obj,k,v)
                    case "input_message_content":
                        imc = self._parse_inputmessagecontent(k,v)
                        setattr(inline_obj,k,imc)
                    case "reply_markup":
                        rep = self._parse_inlinekeyboardobjects(k,v)
                        setattr(inline_obj,k,rep)
                    case _:
                        setattr(inline_obj,k,v)

        elif (key == "inline_query_result_cached_audio"):
            inline_obj = InlineQueryResultCachedAudio()
            for k,v in val.items():
                match k:
                    case "audio_file_id":
                        setattr(inline_obj,k,v)
                    case "input_message_content":
                        imc = self._parse_inputmessagecontent(k,v)
                        setattr(inline_obj,k,imc)
                    case "reply_markup":
                        rep = self._parse_inlinekeyboardobjects(k,v)
                        setattr(inline_obj,k,rep)
                    case _:
                        setattr(inline_obj,k,v)

        elif (key == "inline_query_result_cached_document"):
            inline_obj = InlineQueryResultCachedDocument()
            for k,v in val.items():
                match k:
                    case "document_file_id":
                        setattr(inline_obj,k,v)
                    case "input_message_content":
                        imc = self._parse_inputmessagecontent(k,v)
                        setattr(inline_obj,k,imc)
                    case "reply_markup":
                        rep = self._parse_inlinekeyboardobjects(k,v)
                        setattr(inline_obj,k,rep)
                    case _:
                        setattr(inline_obj,k,v)

        elif (key == "inline_query_result_cached_gif"):
            inline_obj = InlineQueryResultCachedGif()
            for k,v in val.items():
                match k:
                    case "gif_file_id":
                        setattr(inline_obj,k,v)
                    case "input_message_content":
                        imc = self._parse_inputmessagecontent(k,v)
                        setattr(inline_obj,k,imc)
                    case "reply_markup":
                        rep = self._parse_inlinekeyboardobjects(k,v)
                        setattr(inline_obj,k,rep)
                    case _:
                        setattr(inline_obj,k,v)

        elif (key == "inline_query_result_cached_mpeg4_gif"):
            inline_obj = InlineQueryResultCachedMpeg4Gif()
            for k,v in val.items():
                match k:
                    case "mpeg4_file_id":
                        setattr(inline_obj,k,v)
                    case "input_message_content":
                        imc = self._parse_inputmessagecontent(k,v)
                        setattr(inline_obj,k,imc)
                    case "reply_markup":
                        rep = self._parse_inlinekeyboardobjects(k,v)
                        setattr(inline_obj,k,rep)
                    case _:
                        setattr(inline_obj,k,v)

        elif (key == "inline_query_result_cached_photo"):
            inline_obj = InlineQueryResultCachedPhoto()
            for k,v in val.items():
                match k:
                    case "photo_file_id":
                        setattr(inline_obj,k,v)
                    case "input_message_content":
                        imc = self._parse_inputmessagecontent(k,v)
                        setattr(inline_obj,k,imc)
                    case "reply_markup":
                        rep = self._parse_inlinekeyboardobjects(k,v)
                        setattr(inline_obj,k,rep)
                    case _:
                        setattr(inline_obj,k,v)

        elif (key == "inline_query_result_cached_sticker"):
            inline_obj = InlineQueryResultCachedSticker()
            for k,v in val.items():
                match k:
                    case "sticker_file_id":
                        setattr(inline_obj,k,v)
                    case "input_message_content":
                        imc = self._parse_inputmessagecontent(k,v)
                        setattr(inline_obj,k,imc)
                    case "reply_markup":
                        rep = self._parse_inlinekeyboardobjects(k,v)
                        setattr(inline_obj,k,rep)
                    case _:
                        setattr(inline_obj,k,v)

        elif (key == "inline_query_result_cached_video"):
            inline_obj = InlineQueryResultCachedVideo()
            for k,v in val.items():
                match k:
                    case "video_file_id":
                        setattr(inline_obj,k,v)
                    case "input_message_content":
                        imc = self._parse_inputmessagecontent(k,v)
                        setattr(inline_obj,k,imc)
                    case "reply_markup":
                        rep = self._parse_inlinekeyboardobjects(k,v)
                        setattr(inline_obj,k,rep)
                    case _:
                        setattr(inline_obj,k,v)

        elif (key == "inline_query_result_cached_voice"):
            inline_obj = InlineQueryResultCachedVoice()
            for k,v in val.items():
                match k:
                    case "voice_file_id":
                        setattr(inline_obj,k,v)
                    case "input_message_content":
                        imc = self._parse_inputmessagecontent(k,v)
                        setattr(inline_obj,k,imc)
                    case "reply_markup":
                        rep = self._parse_inlin
                        setattr(inline_obj,k,rep)
                    case _:
                        setattr(inline_obj,k,v)

        elif (key == "inline_query_result_contact"):
            inline_obj = InlineQueryResultContact()
            for k,v in val.items():
                match k:
                    case "phone_number"|"first_name"|"last_name"|"thumb_url":
                        setattr(inline_obj,k,v)
                    case "input_message_content":
                        imc = self._parse_inputmessagecontent(k,v)
                        setattr(inline_obj,k,imc)
                    case "reply_markup":
                        rep = self._parse_inlinekeyboardobjects(k,v)
                        setattr(inline_obj,k,rep)
                    case _:
                        setattr(inline_obj,k,v)

        elif (key == "inline_query_result_game"):
            inline_obj = InlineQueryResultGame()
            for k,v in val.items():
                match k:
                    case "game_short_name":
                        setattr(inline_obj,k,v)
                    case "reply_markup":
                        rep = self._parse_inlinekeyboardobjects(k,v)
                        setattr(inline_obj,k,rep)
                    case _:
                        setattr(inline_obj,k,v)

        elif (key == "inline_query_result_gif"):
            inline_obj = InlineQueryResultGif()
            for k,v in val.items():
                match k:
                    case "gif_url"|"thumb_url"|"title"|"caption":
                        setattr(inline_obj,k,v)
                    case "gif_width"|"gif_height"|"gif_duration":
                        setattr(inline_obj,k,int(v))
                    case "input_message_content":
                        imc = self._parse_inputmessagecontent(k,v)
                        setattr(inline_obj,k,imc)
                    case "reply_markup":
                        rep = self._parse_inlinekeyboardobjects(k,v)
                        setattr(inline_obj,k,rep)
                    case _:
                        setattr(inline_obj,k,v)

        elif (key == "inline_query_result_location"):
            inline_obj = InlineQueryResultLocation()
            for k,v in val.items():
                match k:
                    case "latitude"|"longitude"|"title"|"thumb_url":
                        setattr(inline_obj,k,v)
                    case "input_message_content":
                        imc = self._parse_inputmessagecontent(k,v)
                        setattr(inline_obj,k,imc)
                    case "reply_markup":
                        rep = self._parse_inlinekeyboardobjects(k,v)
                        setattr(inline_obj,k,rep)
                    case _:
                        setattr(inline_obj,k,v)

        elif (key == "inline_query_result_mpeg4_gif"):
            inline_obj = InlineQueryResultMpeg4Gif()
            for k,v in val.items():
                match k:
                    case "mpeg4_url"|"thumb_url"|"title"|"caption":
                        setattr(inline_obj,k,v)
                    case "mpeg4_width"|"mpeg4_height"|"mpeg4_duration":
                        setattr(inline_obj,k,int(v))
                    case "input_message_content":
                        imc = self._parse_inputmessagecontent(k,v)
                        setattr(inline_obj,k,imc)
                    case "reply_markup":
                        rep = self._parse_inlinekeyboardobjects(k,v)
                        setattr(inline_obj,k,rep)
                    case _:
                        setattr(inline_obj,k,v)

        elif (key == "inline_query_result_photo"):
            inline_obj = InlineQueryResultPhoto()
            for k,v in val.items():
                match k:
                    case "photo_url"|"thumb_url"|"title"|"caption":
                        setattr(inline_obj,k,v)
                    case "photo_width"|"photo_height":
                        setattr(inline_obj,k,int(v))
                    case "input_message_content":
                        imc = self._parse_inputmessagecontent(k,v)
                        setattr(inline_obj,k,imc)
                    case "reply_markup":
                        rep = self._parse_inlinekeyboardobjects(k,v)
                        setattr(inline_obj,k,rep)
                    case _:
                        setattr(inline_obj,k,v)

        elif (key == "inline_query_result_venue"):
            inline_obj = InlineQueryResultVenue()
            for k,v in val.items():
                match k:
                    case "latitude"|"longitude"|"title"|"address"|"thumb_url":
                        setattr(inline_obj,k,v)
                    case "foursquare_id":
                        setattr(inline_obj,k,v)
                    case "input_message_content":
                        imc = self._parse_inputmessagecontent(k,v)
                        setattr(inline_obj,k,imc)
                    case "reply_markup":
                        rep = self._parse_inlinekeyboardobjects(k,v)
                        setattr(inline_obj,k,rep)
                    case _:
                        setattr(inline_obj,k,v)

        elif (key == "inline_query_result_video"):
            inline_obj = InlineQueryResultVideo()
            for k,v in val.items():
                match k:
                    case "video_url"|"mime_type"|"thumb_url"|"title"|"caption":
                        setattr(inline_obj,k,v)
                    case "video_width"|"video_height"|"video_duration":
                        setattr(inline_obj,k,int(v))
                    case "input_message_content":
                        imc = self._parse_inputmessagecontent(k,v)
                        setattr(inline_obj,k,imc)
                    case "reply_markup":
                        rep = self._parse_inlinekeyboardobjects(k,v)
                        setattr(inline_obj,k,rep)
                    case _:
                        setattr(inline_obj,k,v)

        elif (key == "inline_query_result_voice"):
            inline_obj = InlineQueryResultVoice()
            for k,v in val.items():
                match k:
                    case "voice_url"|"title"|"caption":
                        setattr(inline_obj,k,v)
                    case "voice_duration":
                        setattr(inline_obj,k,int(v))
                    case "input_message_content":
                        imc = self._parse_inputmessagecontent(k,v)
                        setattr(inline_obj,k,imc)
                    case "reply_markup":
                        rep = self._parse_inlinekeyboardobjects(k,v)
                        setattr(inline_obj,k,rep)
                    case _:
                        setattr(inline_obj,k,v)

        return inline_obj

    def _parse_inlinekeyboardobjects(self,key,val) -> InlineKeyboardButton|InlineKeyboardMarkup:
        if (key == "inline_keyboard_button"):
            inline_obj = InlineKeyboardButton()
            for k,v in val.items():
                match k:
                    case "text"|"url"|"callback_data"|"switch_inline_query"|"switch_inline_query_current_chat"|"callback_game"|"pay":
                        setattr(inline_obj,k,v)
                    case _:
                        setattr(inline_obj,k,v)
        elif (key == "inline_keyboard_markup"):
            inline_obj = InlineKeyboardMarkup()
            for k,v in val.items():
                match k:
                    case "inline_keyboard":
                        setattr(inline_obj,k,self._parse_inlinekeyboard(v))
                    case _:
                        setattr(inline_obj,k,v)
        return inline_obj


    def _parse_inputemessagecontents(self,key,val) -> InputMessageContent:
        if (key == "input_text_message_content"):
            input_obj = InputTextMessageContent()
            for k,v in val.items():
                match k:
                    case "message_text"|"parse_mode"|"disable_web_page_preview":
                        setattr(input_obj,k,v)
                    case _:
                        setattr(input_obj,k,v)
        elif (key == "input_location_message_content"):
            input_obj = InputLocationMessageContent()
            for k,v in val.items():
                match k:
                    case "latitude"|"longitude":
                        setattr(input_obj,k,v)
                    case _:
                        setattr(input_obj,k,v)
        elif (key == "input_venue_message_content"):
            input_obj = InputVenueMessageContent()
            for k,v in val.items():
                match k:
                    case "latitude"|"longitude"|"title"|"address"|"foursquare_id":
                        setattr(input_obj,k,v)
                    case _:
                        setattr(input_obj,k,v)
        elif (key == "input_contact_message_content"):
            input_obj = InputContactMessageContent()
            for k,v in val.items():
                match k:
                    case "phone_number"|"first_name"|"last_name":
                        setattr(input_obj,k,v)
                    case _:
                        setattr(input_obj,k,v)
        return input_obj
    
    
    # methods to parse passport objects
    def _parse_passport (self,key:str,val:dict) -> PassportData:
        passport_obj = PassportData()
        for k,v in val.items():
            match k:
                case "data":
                    data = self._parse_passportelement(k,v)
                    setattr(passport_obj,k,data)
                case "credentials":
                    cred = self._parse_encryptedcredentials(k,v)
                    setattr(passport_obj,k,cred)
                case _:
                    setattr(passport_obj,k,v)
        return passport_obj
    
    
    # methods to parse payment objects
    def _parse_payments (self,key:str,val:dict) -> Invoice|SuccessfulPayment:
        payment_obj = None

        if (key == "invoice"):
            payment_obj = Invoice()
            for k,v in val.items():
                setattr(payment_obj,k,v)

        elif (key == "successful_payment"):
            payment_obj = SuccessfulPayment()
            for k,v in val.items():
                setattr(payment_obj,k,v)

        return payment_obj
    
    
    # methods to parse sticker objects
    def _parse_sticker (self,key:str,val:dict) -> Sticker|StickerSet:
        sticker_obj = None

        if (key == "sticker"):
            sticker_obj = Sticker()
            for k,v in val.items():
                match k:
                    case "thumb":
                        thumb = self._parse_photosize(k,v)
                        setattr(sticker_obj,k,thumb)
                    case "mask_position":
                        mask_pos = self._parse_maskposition(k,v)
                        setattr(sticker_obj,k,mask_pos)
                    case _:
                        setattr(sticker_obj,k,v)

        elif (key == "sticker_set"):
            sticker_obj = StickerSet()
            for k,v in val.items():
                match k:
                    case "thumb":
                        thumb = self._parse_photosize(k,v)
                        setattr(sticker_obj,k,thumb)
                    case _:
                        setattr(sticker_obj,k,v)

        return sticker_obj


    def _parse_animation(self,key:str,val:dict) -> Animation:
        animation_obj = Animation()
        for k,v in val.items():
            match k:
                case "thumb":
                    thumb = self._parse_photosize(k,v)
                    setattr(animation_obj,k,thumb)

                case "file_name"|"mime_type":
                    setattr(animation_obj,k,v)

                case "file_size":
                    setattr(animation_obj,k,int(v))
                case _:
                    setattr(animation_obj,k,v)
        return animation_obj

    
    def _parse_audio(self,key:str,val:dict) -> Audio:
        audio_obj = Audio()
        for k,v in val.items():
            match k:
                case "performer"|"title":
                    setattr(audio_obj,k,v)

                case "file_size":
                    setattr(audio_obj,k,int(v))
                case _:
                    setattr(audio_obj,k,v)
        return audio_obj


    def _parse_video(self,key:str,val:dict) -> Video:
        video_obj = Video()
        for k,v in val.items():
            match k:
                case "thumb":
                    thumb = self._parse_photosize(k,v)
                    setattr(video_obj,k,thumb)

                case "file_name"|"mime_type":
                    setattr(video_obj,k,v)

                case "file_size":
                    setattr(video_obj,k,int(v))
                case _:
                    setattr(video_obj,k,v)
        return video_obj

    def _parse_venue(self,key:str,val:dict) -> Venue:
        venue_obj = Venue()
        for k,v in val.items():
            match k:
                case "location":
                    loc = self._parse_location(k,v)
                    setattr(venue_obj,k,loc)
                case "title"|"address"|"foursquare_id":
                    setattr(venue_obj,k,v)
                case _:
                    setattr(venue_obj,k,v)
        return venue_obj

    def _parse_photosize(self,key:str,val:dict) -> PhotoSize:
        photosize_obj = PhotoSize()
        for k,v in val.items():
            match k:
                case "file_size":
                    setattr(photosize_obj,k,int(v))
                case _:
                    setattr(photosize_obj,k,v)
        return photosize_obj

    def _parse_location(self,key:str,val:dict) -> Location:
        location_obj = Location()
        for k,v in val.items():
            match k:
                case "longitude"|"latitude":
                    setattr(location_obj,k,v)
                case _:
                    setattr(location_obj,k,v)
        return location_obj


    def _parse_contact(self,key:str,val:dict) -> Contact:
        contact_obj = Contact()
        for k,v in val.items():
            match k:
                case "phone_number"|"first_name"|"last_name":
                    setattr(contact_obj,k,v)
                case _:
                    setattr(contact_obj,k,v)
        return contact_obj

    def _parse_proximityalerttriggered(self,key:str,val:dict) -> ProximityAlertTriggered:
        proximityalerttriggered_obj = ProximityAlertTriggered()
        for k,v in val.items():
            match k:
                case "traveler"|"watcher"|"distance":
                    setattr(proximityalerttriggered_obj,k,v)
                case _:
                    setattr(proximityalerttriggered_obj,k,v)
        return proximityalerttriggered_obj

    def _parse_login_url(self,key:str,val:dict) -> LoginUrl:
        loginurl_obj = LoginUrl()
        for k,v in val.items():
            match k:
                case "url"|"forward_text"|"bot_username"|"request_write_access":
                    setattr(loginurl_obj,k,v)
                case _:
                    setattr(loginurl_obj,k,v)
        return loginurl_obj


    def _parse_maskposition(self,key:str,val:dict) -> MaskPosition:
        maskposition_obj = MaskPosition()
        for k,v in val.items():
            match k:
                case "point"|"x_shift"|"y_shift"|"scale":
                    setattr(maskposition_obj,k,v)
                case _:
                    setattr(maskposition_obj,k,v)
        return maskposition_obj

    def _parse_inlinekeyboardbutton(self,key:str,val:dict) -> InlineKeyboardButton:
        inlinekeyboardbutton_obj = InlineKeyboardButton()
        for k,v in val.items():
            match k:
                case "text"|"url"|"callback_data"|"switch_inline_query"|"switch_inline_query_current_chat"|"callback_game"|"pay":
                    setattr(inlinekeyboardbutton_obj,k,v)
                case _:
                    setattr(inlinekeyboardbutton_obj,k,v)
        return inlinekeyboardbutton_obj

    def _parse_poll(self,key:str,val:dict) -> Poll:
        poll_obj = None
        
        if (key == "poll"):
            poll_obj = Poll()
            for k,v in val.items():
                match k:
                    case "options":
                        options = []
                        for option in v:
                            options.append(self._parse_polloption(k,option))
                        setattr(poll_obj,k,options)
                    case _:
                        setattr(poll_obj,k,v)
        elif (key == "poll_answer"):
            poll_obj = PollAnswer()
            for k,v in val.items():
                match k:
                    case "poll_id"|"user"|"option_ids":
                        setattr(poll_obj,k,v)
                    case _:
                        setattr(poll_obj,k,v)
        elif (key == "poll_option"):
            poll_obj = PollOption()
            for k,v in val.items():
                match k:
                    case "text":
                        setattr(poll_obj,k,v)
                    case _:
                        setattr(poll_obj,k,v)
        return poll_obj
