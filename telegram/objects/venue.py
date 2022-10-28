from .base import BaseObject

class Venue(BaseObject):
    def __init__(self,
        location,
        title,
        address,
        foursquare_id = None,
        foursquare_type = None,
        google_place_id = None,
        google_place_type = None,
        ):

        self.location = location
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type
        self.google_place_id = google_place_id
        self.google_place_type = google_place_type
