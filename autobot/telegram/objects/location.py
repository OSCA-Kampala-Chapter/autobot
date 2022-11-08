from autobot.telegram.objects.base import BaseObject

class Location(BaseObject):
    """
    This object represents a point on the map.

    Args:
        longitude (float): Longitude as defined by sender
        latitude (float): Latitude as defined by sender
    """
    
    __slots__ = ("longitude","latitude")
    
    def __init__(self, longitude: float = None, latitude: float = None) -> None:
        self.longitude = longitude
        self.latitude = latitude

    