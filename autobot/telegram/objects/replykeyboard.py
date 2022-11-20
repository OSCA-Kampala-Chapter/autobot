from autobot.telegram.objects.base import BaseObject
from autobot.telegram.objects.keyboardbutton import KeyboardButton


class ReplyKeyboardMarkup(BaseObject):
    """
    This object represents a custom keyboard with reply options (see Introduction to bots for details and examples).

    Args:
        keyboard (list): Array of button rows, each represented by an Array of KeyboardButton objects
        resize_keyboard (bool): Optional. Requests clients to resize the keyboard vertically for optimal fit (e.g., make the keyboard smaller if there are just two rows of buttons). Defaults to False, in which case the custom keyboard is always of the same height as the app's standard keyboard.
        one_time_keyboard (bool): Optional. Requests clients to hide the keyboard as soon as it's been used. The keyboard will still be available, but clients will automatically display the usual letter-keyboard in the chat – the user can press a special button in the input field to see the custom keyboard again. Defaults to False.
        selective (bool): Optional. Use this parameter if you want to show the keyboard to specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id), sender of the original message. Example: A user requests to change the bot‘s language, bot replies to the request with a keyboard to select the new language. Other users in the group don’t see the keyboard.
    """

    __slots__ = (
        'keyboard',
        'resize_keyboard',
        'one_time_keyboard',
        'selective'
    )

    def __init__(self, keyboard: list[list[KeyboardButton]] = None) -> None:
        self.keyboard = keyboard
        self.resize_keyboard: bool = None
        self.one_time_keyboard: bool = None
        self.selective: bool = None


class ReplyKeyboardRemove(BaseObject):
    """
    Upon receiving a message with this object, Telegram clients will remove the current custom keyboard and display the default letter-keyboard. By default, custom keyboards are displayed until a new keyboard is sent by a bot. An exception is made for one-time keyboards that are hidden immediately after the user presses a button (see ReplyKeyboardMarkup).

    Args:
        remove_keyboard (bool): Requests clients to remove the custom keyboard (user will not be able to summon this keyboard; if you want to hide the keyboard from sight but keep it accessible, use one_time_keyboard in ReplyKeyboardMarkup)
        selective (bool): Optional. Use this parameter if you want to remove the keyboard for specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id), sender of the original message. Example: A user votes in a poll, bot returns confirmation message in reply to the vote and removes the keyboard for that user, while still showing the keyboard with poll options to users who haven't voted yet.
    """

    __slots__ = (
        'remove_keyboard',
        'selective',
    )

    def __init__(self, remove_keyboard: bool = None) -> None:
        self.remove_keyboard = remove_keyboard
        self.selective: bool | None = None
