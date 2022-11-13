from autobot.telegram.objects import *
from autobot.telegram.games.objects import *
from autobot.telegram.inline.objects import *
from autobot.telegram.passport.objects import *
from autobot.telegram.payments.objects import *
from autobot.telegram.stickers.objects import *

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
                    qry = self._parse_inline(k,v)
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
                        rep = self._parse_inline(k,v)
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
    
    
    
    # methods to parse passport objects
    
    
    # methods to parse payment objects
    
    
    # methods to parse sticker objects

