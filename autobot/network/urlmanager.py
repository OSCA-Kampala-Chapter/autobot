"""
This module handles construction of urls needed for making queries
"""
from urllib.parse import urlsplit,urlunsplit

__all__ = ("UrlManager")

class UrlManager:

    def __init__ (self,token):
        self.token = "bot" + str(token) + "/"
        self.url_parts = ["https","api.telegram.org","","",""]
        self.url = "/".join((urlunsplit(self.url_parts),self.token))

    def add_method (self,other):
        """
        append other part onto the url string
        """
        sch,netloc,path,qry,frag = urlsplit(self.url)
        try:
            base,method = path.split("/")
        except ValueError:
            prev,base,method = path.split("/")
        path = "/".join([base,other])
        self.url = urlunsplit((sch,netloc,path,qry,frag))
        return self.url

    def add_query (self,**kwargs):
        """
        append queries to the query part of the url
        """
        params = ["=".join([str(k),str(v)]) for k,v in kwargs.items()]
        qry_string = "&".join(params)
        sch,netloc,path,qry,frag = urlsplit(self.url)
        qry = qry_string
        return urlunsplit([sch,netloc,path,qry,frag])