from autobot.telegram.objects.base import BaseObject
from typing import Optional

class Contact(BaseObject):

    """
        This object represents a phone contact.

        Args:
            phone_number (str) : Contact's phone number

            first_name (str) : Contact's first name
            
            last_name (str) : Optional. Contact's last name

            user_id (int) : Optional. Contact's user identifier in Telegram. 
            This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. 
            But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.

            vcard (str) : Optional. Additional data about the contact in the form of a vCard

    """
    
    __slots__ = ("phone_number",
                "first_name",
                "last_name",
                "user_id",
                "vcard",
                )

    def __init__(self, phone_number:str = None, first_name:str = None) -> None:
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name: Optional[str] = None
        self.user_id: Optional[int] = None
        self.vcard: Optional[str] = None

