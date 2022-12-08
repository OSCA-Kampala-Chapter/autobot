"""
This module contains a class with methods representing the passport api
"""

class PassportAPI:
    
    async def set_passport_data_errors(self, **kwargs):
        """
        Use this if you encounter data that doesn't satisfy the requirements of the data fields that you provided to users. 
        On success, True is returned.
        """
        url = self.url.add_method("setPassportDataErrors")
        res = await self._post(url=url, body=kwargs)
        return self.parser.parse(res)

    async def delete_passport_element(self, **kwargs):
        """
        Use this to delete a Telegram Passport element; for bots only. 
        Returns True on success.
        """
        url = self.url.add_method("deletePassportElement")
        res = await self._post(url=url, body=kwargs)
        return self.parser.parse(res)

    async def set_passport_element_errors(self, **kwargs):
        """
        Use this to add some errors to a Telegram Passport element; for bots only. 
        Returns True on success.
        """
        url = self.url.add_method("setPassportElementErrors")
        res = await self._post(url=url, body=kwargs)
        return self.parser.parse(res)

    async def get_passport_element(self, **kwargs):
        """
        Use this to request Telegram Passport data for a user. 
        Returns a Telegram PassportElement on success.
        """
        url = self.url.add_method("getPassportElement")
        res = await self._post(url=url, body=kwargs)
        return self.parser.parse(res)

    async def get_passport_authorization_form(self, **kwargs):
        """
        Use this method to request Telegram Passport data for a user. 
        Returns a Telegram PassportAuthorizationForm on success.
        """
        url = self.url.add_method("getPassportAuthorizationForm")
        res = await self._get(url=url, body=kwargs)
        return self.parser.parse(res)

    async def send_passport_authorization_form(self, **kwargs):
        """
        Use this method to send a Telegram Passport authorization form for sharing data with a service. 
        Returns True on success.
        """
        url = self.url.add_method("sendPassportAuthorizationForm")
        res = await self._post(url=url, body=kwargs)
        return self.parser.parse(res)

    async def get_passport_data(self, **kwargs):
        """
        Use this method to request Telegram Passport data for a user. 
        Returns a Telegram PassportData on success.
        """
        url = self.url.add_method("getPassportData")
        res = await self._get(url=url, body=kwargs)
        return self.parser.parse(res)

    async def set_passport_data(self, **kwargs):
        """
        Use this method to send a Telegram Passport authorization form for sharing data with a service. 
        Returns True on success.
        """
        url = self.url.add_method("setPassportData")
        res = await self._post(url=url, body=kwargs)
        return self.parser.parse(res)

