from ..objects import BaseObject

class Sticker(BaseObject):

    """
        This object represents a sticker

        Args:
            file_id (str) : Identifier for this file, which can be used to download or reuse the file

            file_unique_id (str) : Unique identifier for this file, which is supposed to be the same over time and for different bots. 
            Can't be used to download or reuse the file.

            type (str) : Type of the sticker, currently one of “regular”, “mask”, “custom_emoji”. 
            The type of the sticker is independent from its format, which is determined by the fields is_animated and is_video.

            width (int) : Sticker width

            height (int) : Sticker height

            is_animated : 	True, if the sticker is animated

            is_video : True, if the sticker is a video sticker

            thumb (:obj: `PhotoSize`, optional) : Optional. Sticker thumbnail in the .WEBP or .JPG format

            emoji (str): Optional. Emoji associated with the sticker

            set_name (str) : Optional. Name of the sticker set to which the sticker belongs

            premium animation (:obj: `File`, optional) : Optional. For premium regular stickers, premium animation for the sticker

            mask_postion (:obj: `MaskPosition`, optional) : Optional. For mask stickers, the position where the mask should be placed

            custom_emoji_id (str) : Optional. For custom emoji stickers, unique identifier of the custom emoji

            file_size (int) : Optional. File size in bytes

    """

    __slots__ = ("file_id",
                "file_unique_id",
                "type",
                "width",
                "height",
                "is_animated",
                "is_video",
                "thumb",
                "emoji",
                "set_name",
                "premium_animation",
                "mask_position",
                "custom_emoji_id",
                "file_size",
                )

    def __init__(self, file_id, file_unique_id, type, width, height, is_animated, is_video):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.type = type
        self.width = width
        self.height = height
        self.is_animated = is_animated
        self.is_video = is_video
        self.thumb = None
        self.emoji = None
        self.set_name = None
        self.premium_animation = None
        self.mask_position = None
        self.custom_emoji_id = None
        self.file_size = None


class StickerSet(BaseObject):

    """
        This object represents a sticker set.

        Args:
            
            name (str) : Sticker set name

            title (str): Sticker set title

            sticker_type (str) : Type of stickers in the set, currently one of “regular”, “mask”, “custom_emoji”

            is_animated (bool) : True, if the sticker set contains animated stickers

            is_video (bool) : True, if the sticker set contains video stickers

            sticker (:obj:  `List[Sticker]`) : List of all set stickers.

            thumb (:obj: `PhotoSize`, optional) : Optional. Sticker thumbnail in the .WEBP or .JPG format.

    """

    __slots__ = ("name",
                "title",
                "sticker_type",
                "is_animated",
                "is_video",
                "stickers",
                "thumb",
                )

    def __init__(self, name, title, sticker_type, is_animated, is_video, stickers):
        self.name = name
        self.title = title
        self.sticker_type = sticker_type
        self.is_animated = is_animated
        self.is_video = is_video
        self.stickers = stickers
        self.thumb = None


class MaskPosition(BaseObject):

    """
        This object describes the position on faces where a mask should be placed by default.

        Args:

            point (str): The part of the face relative to which the mask should be placed. 
            One of “forehead”, “eyes”, “mouth”, or “chin”.

            x_shift (float) : Shift by X-axis measured in widths of the mask scaled to the face size, from left to right. 
            For example, choosing -1.0 will place mask just to the left of the default mask position.

            y_shift (float) : Shift by Y-axis measured in heights of the mask scaled to the face size, from top to bottom. 
            For example, 1.0 will place the mask just below the default mask position.

            scale (float) : Mask scaling coefficient. For example, 2.0 means double size.

    """

    __slots__ = ("point",
                "x_shift",
                "y_shift",
                "scale",
                )

    def __init__(self, point, x_shift, y_shift, scale):
        self.point = point
        self.x_shift = x_shift
        self.y_shift = y_shift
        self.scale = scale


