import httpx
api_url = "http://localhost:8000"

async def login_request(email: str, password: str):
    limits = httpx.Timeout(5.0, read=10.0)
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{api_url}/users/auth/login", 

            data={'username': email, 'password': password} 
        )
        return response.status_code, response.json()