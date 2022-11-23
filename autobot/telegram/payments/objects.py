from autobot.telegram.objects import BaseObject, User
from typing import Optional

class LabeledPrice(BaseObject):

    """
        This object represents a portion of the price for goods or services.

        Args:

            label (str) : Portion label

            amount (int) : Price of the product in the smallest units of the currency (integer, not float/double). 
            For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, 
            it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).

    """


    def __init__(self, label: str = None, amount: int = None) -> None:
        self.label = label
        self.amount = amount


class Invoice(BaseObject):

    """
        This object contains basic information about an invoice.

        Args:
            title (str) : Product name

            description (str) : Product description

            start_parameter (str) : Unique bot deep-linking parameter that can be used to generate this invoice

            currency (str) : Three-letter ISO 4217 currency code

            total_ampount (int) : 	Total price in the smallest units of the currency (integer, not float/double). 
            For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, 
            it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).

    """


    def __init__(self, title: str = None, description: str = None, start_parameter: str = None, currency: str = None, total_amount: int = None) -> None:
        self.title = title
        self.description = description
        self.start_parameter = start_parameter
        self.currency = currency
        self.total_amount = total_amount


class ShippingAddress(BaseObject):

    """

        This object represents a shipping address.

        Args:
            country_code (str) : Two-letter ISO 3166-1 alpha-2 country code

            state (str) : State, if applicable

            city (str) : City

            street_line1 (str) : First line for the address

            street_line2 (str) : Second line for the address

            post_code (str) : Address post code
    
    """


    def __init__(self, country_code: str = None, state: str = None, city: str = None, street_line1: str = None, street_line2: str = None, post_code: str = None) -> None:
        self.country_code = country_code
        self.state = state
        self.city = city
        self.street_line1 = street_line1
        self.street_line2 = street_line2
        self.post_code = post_code


class OrderInfo(BaseObject):

    """
        Args:

            name (str) : Optional. User name

            phone_number (str) : Optional. User's phone number

            email (str) :Optional. User email

            shipping_address (:obj :`ShippingAddress`) : Optional. User shipping address

    """


    def __init__(self):
        self.name: Optional[str] = None
        self.phone_number: Optional[str] = None
        self.email: Optional[str] = None
        self.shipping_address: Optional[ShippingAddress] = None


class ShippingOption(BaseObject):

    """

        This object represents one shipping option.

        Args:

            id (str) : Shipping option identifier

            title (str) : Option title

            prices (:obj :list[`LabeledPrice`] ) : list of price portions
    """


    def __init__(self, id: str = None, title: str = None, prices: list[LabeledPrice] = None) -> None:
        self.id = id
        self.title = title
        self.prices = prices


class SuccessfulPayment(BaseObject):

    """

        This object contains basic information about a successful payment.

        Args:
            currency (str) : Three-letter ISO 4217 currency code

            total_amount : Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).

            invoice_payload (str) : Bot specified invoice payload

            shipping_option_id (str) : Optional. Identifier of the shipping option chosen by the user

            order_info (:obj :`OrderInfo`) : Optional. Order information provided by the user

            telegram_payment_charge_id (str) : Telegram payment identifier

            provider_payment_charge_id (str) : Provider payment identifier
    
    """


    def __init__(self, currency: str = None, total_amount: int = None, invoice_payload: str = None, telegram_payment_charge_id: str = None, provider_payment_charge_id: str = None) -> None:
        self.currency = currency
        self.total_amount = total_amount
        self.invoice_payload = invoice_payload
        self.telegram_payment_charge_id = telegram_payment_charge_id
        self.provider_payment_charge_id = provider_payment_charge_id
        self.shipping_option_id: Optional[str] = None
        self.order_info: Optional[OrderInfo] = None



class ShippingQuery(BaseObject):

    """
        This object contains information about an incoming shipping query.

        Args:

            id (str) : 	Unique query identifier

            sent_from (:obj :`User`) : User who sent the query

            invoice_payload (str) : Bot specified invoice payload

            shipping_address (:obj :`ShippingAddress`) : User specified shipping address

        Special Note:
            ShippingQuery object species `from` as an argument which comflicts with the `from`, the default
            import statement of Python. 

            Used `sent_from` as an alias to `from`
    
    """


    def __init__(self, id: str = None, sent_from: User = None, invoice_payload: str = None, shipping_address: ShippingAddress = None) -> None:
        self.id = id
        self.sent_from = sent_from
        self.invoice_payload = invoice_payload
        self.shipping_address = shipping_address


class PreCheckoutQuery(BaseObject):

    """

        This object contains information about an incoming pre-checkout query.

        Args:

            id (str) : 	Unique query identifier

            sent_from (:obj :`User`) : User who sent the query

            currency (str) : Three-letter ISO 4217 currency code

            total_amount (int) : Total price in the smallest units of the currency (integer, not 
            float/double). For example, for a price of US$ 1.45 pass amount = 145. 
            See the exp parameter in currencies.json, it shows the number of digits past 
            the decimal point for each currency (2 for the majority of currencies).

            invoice_payload (str) : Bot specified invoice payload

            shipping_option_id (str) : Optional. Identifier of the shipping option chosen by the user

            order_info (:obj :`OrderInfo`) : Optional. Order information provided by the user

        Special Note:
            PreCheckoutQuery object species `from` as an argument which comflicts with the `from`, the default
            import statement of Python. 

            Used `sent_from` as an alias to `from`

    """

    def __init__(self, id: str = None, sent_from: User = None, currency: str = None, total_amount: int = None, invoice_payload: str = None) -> None:
        self.id = id
        self.sent_from = sent_from
        self.currency =currency
        self.total_amount = total_amount
        self.invoice_payload = invoice_payload
        self.shipping_option_id: Optional[str] = None
        self.order_info: Optional[OrderInfo] = None