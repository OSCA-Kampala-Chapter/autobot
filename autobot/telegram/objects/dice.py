from .base import BaseObject

class Dice(BaseObject):
    
    """
        This object represents an animated emoji that displays a random value.

        Args:
            emoji (str) : Emoji on which the dice throw animation is based

            value (int) : Value of the dice, 1-6 for “🎲”, “🎯” and “🎳” base emoji, 1-5 for “🏀” and “⚽” base emoji, 1-64 for “🎰” base emoji

    """

    __slots__ = ("emoji", "value",)

    def __init__(self, emoji:str, value:int):
        self.emoji = emoji
        self.value = value
