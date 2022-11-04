from .objects import BaseObject

class PassportData(BaseObject):
    """Describes Telegram Passport data shared with the bot by the user.

    Args:
        data (list): A List with information about documents and other Telegram Passport elements that was shared with the bot

        credentials (str): Encrypted credentials required to decrypt the data
    """
    def __init__(self, data:list, credentials:str) -> None:
        self.data = data 
        self.credentials = credentials

class PassportFile(BaseObject):
    """This object represents a file uploaded to Telegram Passport. Currently all Telegram Passport files are in JPEG format when decrypted and don't exceed 10MB.

        Args:
            file_id (str): Identifier for this file, which can be used to download or reuse the file.
            file_unique_id (str): Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
            file_size (int): File size in bytes.
            file_date (int): Unix time when the file was uploaded.
    """

    def __init__(self, file_id:str, file_unique_id:str, file_size:int, file_date:int):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.file_size = file_size
        self.file_date = file_date

class EncryptedPassportElement(BaseObject):
    """Describes documents or other Telegram Passport elements shared with the bot by the user.

        Args:
            type (str): Element type. One of “personal_details”, “passport”, “driver_license”, “identity_card”, “internal_passport”, “address”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”, “phone_number”, “email”.
            hash (str): Base64-encoded element hash for using in PassportElementErrorUnspecified
            data (str): Optional. Base64-encoded encrypted Telegram Passport element data provided by the user, available for “personal_details”, “passport”, “driver_license”, “identity_card”, “internal_passport” and “address” types. Can be decrypted and verified using the accompanying EncryptedCredentials.
            phone_number (str):  Optional. User's verified phone number, available only for “phone_number” type.
            email (str): Optional. User's verified email address, available only for “email” type.
            files (list): Optional. A list of encrypted files with documents provided by the user, available for “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration” and “temporary_registration” types. Files can be decrypted and verified using the accompanying EncryptedCredentials.
            front_side (PassportFile): Optional. Encrypted file with the front side of the document, provided by the user. Available for “passport”, “driver_license”, “identity_card” and “internal_passport”. The file can be decrypted and verified using the accompanying EncryptedCredentials.
            reverse_side (PassportFile): Optional. Encrypted file with the reverse side of the document, provided by the user. Available for “driver_license” and “identity_card”. The file can be decrypted and verified using the accompanying EncryptedCredentials.
            selfie (PassportFile): Optional. Encrypted file with the selfie of the user holding a document, provided by the user; available for “passport”, “driver_license”, “identity_card” and “internal_passport”. The file can be decrypted and verified using the accompanying EncryptedCredentials.
            translation (list): Optional. A list of encrypted files with translated versions of documents provided by the user. Available if requested for “passport”, “driver_license”, “identity_card”, “internal_passport”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration” and “temporary_registration” types. Files can be decrypted and verified using the accompanying EncryptedCredentials.

    """
    __slots__ = (
        "data",
        "phone_number",
        "email",
        "files",
        "front_side",
        "reverse_side",
        "selfie",
        "translation",
        
    )
    def __init__(self, type:str, hash:str):
        self.type = type
        self.hash = hash

class EncryptedCredentials(BaseObject):
    """Describes data required for decrypting and authenticating EncryptedPassportElement.

        Args:
            data (str): Base64-encoded encrypted JSON-serialized data with unique user's payload, data hashes and secrets required for EncryptedPassportElement decryption and authentication.
            hash (str): Base64-encoded data hash for data authentication.
            secret (str): Base64-encoded secret, encrypted with the bot's public RSA key, required for data decryption.
    """

    def __init__(self, data:str, hash:str, secret:str):
        self.data = data
        self.hash = hash
        self.secret = secret

class PassportElementErrorDataField(BaseObject):
    """Represents an issue in one of the data fields that was provided by the user. The error is considered resolved when the field's value changes.

        Args:
            source (str): Error source, must be data.
            type (str): The section of the user's Telegram Passport which has the error, one of “personal_details”, “passport”, “driver_license”, “identity_card”, “internal_passport”, “address”.
            field_name (str): Name of the data field which has the error.
            data_hash (str): Base64-encoded data hash.
            message (str): Error message.
    """

    def __init__(self, source:str, type:str, field_name:str, data_hash:str, message:str):
        self.source = source
        self.type = type
        self.field_name = field_name
        self.data_hash = data_hash
        self.message = message

class PassportElementErrorFrontSide(BaseObject):
    """Represents an issue with the front side of a document. The error is considered resolved when the file with the front side of the document changes.

        Args:
            source (str): Error source, must be front_side.
            type (str): The section of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”.
            file_hash (str): Base64-encoded hash of the file with the front side of the document.
            message (str): Error message.
    """

    def __init__(self, source:str, type:str, file_hash:str, message:str):
        self.source = source
        self.type = type
        self.file_hash = file_hash
        self.message = message

class PassportElementErrorReverseSide(BaseObject):
    """Represents an issue with the reverse side of a document. The error is considered resolved when the file with reverse side of the document changes.

        Args:
            source (str): Error source, must be reverse_side.
            type (str): The section of the user's Telegram Passport which has the issue, one of “driver_license”, “identity_card”.
            file_hash (str): Base64-encoded hash of the file with the reverse side of the document.
            message (str): Error message.
    """

    def __init__(self, source:str, type:str, file_hash:str, message:str):
        self.source = source
        self.type = type
        self.file_hash = file_hash
        self.message = message

class PassportElementErrorSelfie(BaseObject):
    """Represents an issue with the selfie with a document. The error is considered resolved when the file with the selfie changes.

        Args:
            source (str): Error source, must be a selfie.
            type (str): The section of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”.
            file_hash (str): Base64-encoded hash of the file with the selfie.
            message (str): Error message.
    """

    def __init__(self, source:str, type:str, file_hash:str, message:str):
        self.source = source
        self.type = type
        self.file_hash = file_hash
        self.message = message

class PassportElementErrorFile(BaseObject):
    """Represents an issue with a document scan. The error is considered resolved when the file with the document scan changes.

        Args:
            source (str): Error source, must be a file.
            type (str): The section of the user's Telegram Passport which has the issue, one of “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”.
            file_hash (str): Base64-encoded file hash.
            message (str): Error message.
    """

    def __init__(self, source:str, type:str, file_hash:str, message:str):
        self.source = source
        self.type = type
        self.file_hash = file_hash
        self.message = message
        
class PassportElementErrorFiles(BaseObject):
    """Represents an issue with a list of scans. The error is considered resolved when the list of files containing the scans changes.

        Args:
            source (str): Error source, must be files.
            type (str):  	The section of the user's Telegram Passport which has the issue, one of “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”.
            file_hash (list): List of base64-encoded file hashes.
            message (str): Error message.
    """

    def __init__(self, source:str, type:str, file_hash:list, message:str):
        self.source = source
        self.type = type
        self.file_hash = file_hash
        self.message = message

class PassportElementErrorTranslationFile(BaseObject):
    """Represents an issue with one of the files that constitute the translation of a document. The error is considered resolved when the file changes.

        Args:
            source (str): Error source, must be a translation_file.
            type (str): Type of element of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”.
            file_hash (str): Base64-encoded file hash.
            message (str): Error message.
    """

    def __init__(self, source:str, type:str, file_hash:str, message:str):
        self.source = source
        self.type = type
        self.file_hash = file_hash
        self.message = message
        
class PassportElementErrorTranslationFiles(BaseObject):
    """Represents an issue with the translated version of a document. The error is considered resolved when a file with the document translation change.

        Args:
            source (str): Error source, must be translation_files.
            type (str): Type of element of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”.
            file_hash (list): List of base64-encoded file hashes.
            message (str): Error message.
    """

    def __init__(self, source:str, type:str, file_hash:list, message:str):
        self.source = source
        self.type = type
        self.file_hash = file_hash
        self.message = message

class PassportElementErrorUnspecified(BaseObject):
    """Represents an issue in an unspecified place. The error is considered resolved when new data is added.

        Args:
            source (str): Error source, must be unspecified.
            type (str): Type of element of the user's Telegram Passport which has the issue.
            element_hash (str): Base64-encoded element hash.
            message (str): Error message.
    """

    def __init__(self, source:str, type:str, element_hash:str, message:str):
        self.source = source
        self.type = type
        self.element_hash = element_hash
        self.message = message
        