import pytest
import time
import asyncio
import aiohttp

from pygti.auth import Auth
from pygti.gti import *
from pygti.schemas import TariffRequest
from tests.payloadsForTesting import payloadsTariffRequest


class test_TariffRequest:
    @pytest.mark.schema
    def test_Schema_TariffRequest_CorrectExamples(self):
        for payload in payloadsTariffRequest:
            tariff = TariffRequest(payload)
        assert True

    @pytest.mark.asyncio
    async def test_Asyncio_CNRequest(self, enterCredentials):
        async with aiohttp.ClientSession() as session:
            gti_user = enterCredentials[0]
            gti_pass = enterCredentials[1]
            auth = Auth(session, gti_user, gti_pass)
            gti = GTI(auth)

            for payload in payloadsTariffRequest:
                tariff = await gti.getTariff(payload)
                time.sleep(1)

        assert True
