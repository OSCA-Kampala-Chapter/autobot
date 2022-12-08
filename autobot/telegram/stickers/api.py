"""
This module contains a class with methods representing the sticker methods
"""

class StickerAPI:

    async def get_sticker_set(self,**kwargs):
        url = self.url.add_method("getStickerSet")
        res = await self._get(url = url,headers = kwargs)
        return self.parser.parse(res)

    async def upload_sticker_file(self,**kwargs):
        url = self.url.add_method("uploadStickerFile")
        res = await self._post(url = url,body = kwargs)
        return self.parser.parse(res)

    async def create_new_sticker_set(self,**kwargs):
        url = self.url.add_method("createNewStickerSet")
        res = await self._post(url = url,body = kwargs)
        return self.parser.parse(res)

    async def add_sticker_to_set(self,**kwargs):
        url = self.url.add_method("addStickerToSet")
        res = await self._post(url = url,body = kwargs)
        return self.parser.parse(res)

    async def set_sticker_position_in_set(self,**kwargs):
        url = self.url.add_method("setStickerPositionInSet")
        res = await self._post(url = url,body = kwargs)
        return self.parser.parse(res)
        
    async def delete_sticker_from_set(self,**kwargs):
        url = self.url.add_method("deleteStickerFromSet")
        res = await self._post(url = url,body = kwargs)
        return self.parser.parse(res)

    async def set_sticker_set_thumb(self,**kwargs):
        url = self.url.add_method("setStickerSetThumb")
        res = await self._post(url = url,body = kwargs)
        return self.parser.parse(res)

