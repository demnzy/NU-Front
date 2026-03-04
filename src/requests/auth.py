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
    
async def signup_request(email: str, username: str, password: str, first_name: str, last_name: str, gender: str, role: str, organisation: dict | None = None):
    
    payload = {
        "username": username,
        "email": email,
        "password": password,
        "first_name": first_name,
        "last_name": last_name,
        "gender": gender,
        "role": role
    }

    if organisation is not None:
        payload["organisation"] = organisation

    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.post(
            f"{api_url}/users/auth/register", 
            json=payload 
        )
        return response.status_code, response.json()