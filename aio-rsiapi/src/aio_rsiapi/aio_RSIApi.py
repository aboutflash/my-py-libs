import json
from enum import Enum
from typing import Optional

from aiohttp import ClientSession, hdrs

from aio_rsiapi import to_json
from aio_rsiapi.core import NoCorsApi


class RSIMemberAutocomplete(NoCorsApi):
    """
    This implementation gains access to the member search autocompletion API of
    the RSI Spectrum site.
    """

    def __init__(self):
        super(RSIMemberAutocomplete, self).__init__(
            r'https://robertsspaceindustries.com/api/spectrum/search/member/autocomplete')

    @staticmethod
    def construct_payload(search_str):
        return {'community_id': None, 'text': search_str, 'ignore_self': False}

    async def get_raw(self, search_str) -> Optional[bytes]:
        async with ClientSession(json_serialize=json.dumps) as session, \
                session.post(self.get_endpoint().geturl(),
                             json=self.construct_payload(search_str)) as response:
            return await response.read()

    async def get_json(self, search_str) -> dict:
        response_data = await self.get_raw(search_str)
        full_json_response = to_json(response_data)
        return full_json_response['data']


class RSIFundingStats(NoCorsApi):
    """
    Receives the current funding statistics from the RSI website API endpoint.
    """

    class TimeFrame(str, Enum):
        MONTH = 'month'
        WEEK = 'week'
        DAY = 'day'
        HOUR = 'hour'

    def __init__(self):
        super(RSIFundingStats, self).__init__(r'https://robertsspaceindustries.com/api/stats/getCrowdfundStats')

    @staticmethod
    def construct_payload(time_frame: str):
        return {"chart": time_frame, "fans": True, "funds": True, "alpha_slots": True, "fleet": True}

    async def get_raw(self, time_frame: TimeFrame = TimeFrame.DAY) -> Optional[bytes]:
        async with ClientSession(json_serialize=json.dumps,
                                 headers={hdrs.ACCEPT_ENCODING: 'gzip'}) as session, \
                session.post(self.get_endpoint().geturl(), json=self.construct_payload(time_frame)) as response:
            return await response.read()

    async def get_json(self, time_frame: TimeFrame = TimeFrame.DAY) -> dict:
        response_data = await self.get_raw(time_frame)
        full_json_response = to_json(response_data)
        return full_json_response['data']
