import asyncio
import unittest

from aio_rsiapi.aio_RSIApi import RSIFundingStats, RSIMemberAutocomplete


class EndPointTest(unittest.IsolatedAsyncioTestCase):
    """
    A library test against the real remote API endpoints.
    No further mocking for simplicity.
    """
    loop = None

    def setUp(self):
        pass

    async def asyncSetUp(self):
        pass

    async def test_funds_api(self):
        proxy = RSIFundingStats()
        response = await proxy.get_json(RSIFundingStats.TimeFrame.DAY)
        self.assertGreater(response.get('funds'), 0, "Funds retrieved should be greater than 0")
        self.addAsyncCleanup(self.on_cleanup)

    async def test_autocomplete_api(self):
        proxy = RSIMemberAutocomplete()
        response = await proxy.get_json('huhu')
        self.assertGreater(len(response.get('members')), 0)
        self.addAsyncCleanup(self.on_cleanup)

    async def asyncTearDown(self):
        pass

    def tearDown(self) -> None:
        pass

    @staticmethod
    async def on_cleanup():
        await asyncio.sleep(0.1)


if __name__ == '__main__':
    unittest.main()
