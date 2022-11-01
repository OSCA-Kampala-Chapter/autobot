from .base import BaseObject

class Location(BaseObject):
    """
    This object represents a point on the map.

    Args:
        longitude (float): Longitude as defined by sender
        latitude (float): Latitude as defined by sender
    """

    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude

    