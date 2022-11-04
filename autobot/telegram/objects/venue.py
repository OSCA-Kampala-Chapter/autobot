from . import Location
from .base import BaseObject

class Venue(BaseObject):
    """
    This object represents a venue.

    Args:
        location (Location): Venue location

        title (str): Name of the venue

        address (str): Address of the venue

        foursquare_id (Optional[str]): Optional. Foursquare identifier of the venue

        foursquare_type (Optional[str]): Optional. Foursquare type of the venue. 
        (For example, "arts_entertainment/default", "arts_entertainment/aquarium" or "food/icecream".)

        google_place_id (Optional[str]): Optional. Google Places identifier of the venue
        
        google_place_type (Optional[str]): Optional. Google Places type of the venue. (See supported types.)
    """

    __slots__ = (
        'location', 
        'title', 
        'address', 
        'foursquare_id', 
        'foursquare_type', 
        'google_place_id', 
        'google_place_type'
        )
    
    
    def __init__(self, location, title, address):
        self.location = location
        self.title = title
        self.address = address
        self.foursquare_id = None
        self.foursquare_type = None
        self.google_place_id = None
        self.google_place_type = None

 