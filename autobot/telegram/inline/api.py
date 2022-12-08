"""
This module contains a class with methods representing the inline api
"""

class InlineAPI:
    
    async def answer_inline_query(self, **kwargs):
        url = self.url.add_method("answerInlineQuery")
        res = await self._post(url=url, body=kwargs)
        return self.parser.parse(res)

