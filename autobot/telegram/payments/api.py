"""
This module contains a class with methods representing the payments api
"""
class PaymentsAPI:
    
    async def send_invoice(self, **kwargs):
        url = self.url.add_method("sendInvoice")
        res = await self._post(url=url, body=kwargs)
        return self.parser.parse(res)

    
    async def answer_shipping_query(self, **kwargs):
        url = self.url.add_method("answerShippingQuery")
        res = await self._post(url=url, body=kwargs)
        return self.parser.parse(res)


    async def answer_pre_checkout_query(self, **kwargs):
        url = self.url.add_method("answerPreCheckoutQuery")
        res = await self._post(url=url, body=kwargs)
        return self.parser.parse(res)
        
