"""
This module contains a class with methods representing the games api
"""
class GamesAPI:
    
    async def get_game_high_scores(self, **kwargs):
        url = self.url.add_method("getGameHighScores")
        res = await self._post(url=url, body=kwargs)
        return self.parser.parse(res)

    async def set_game_score(self, **kwargs):
        url = self.url.add_method("setGameScore")
        res = await self._post(url=url, body=kwargs)
        return self.parser.parse(res)

    async def send_game(self, **kwargs):
        url = self.url.add_method("sendGame")
        res = await self._post(url=url, body=kwargs)
        return self.parser.parse(res)

