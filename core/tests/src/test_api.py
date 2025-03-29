from http import HTTPStatus 
import pytest
import aiohttp

class TestApi:
    
    @pytest.mark.asyncio(loop_scope="session")
    async def test_add_api(self):
        session =aiohttp.ClientSession()
        req_url = "http://localhost:8000/api/v1/roles/create_role/"
        query_data = {"name": "admin", "level": 5}

        response = await session.request(
            "POST",
            req_url,
            json=query_data,
            params=None

        )

        assert response.status == HTTPStatus.ACCEPTED