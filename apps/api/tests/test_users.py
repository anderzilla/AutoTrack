import pytest
import time

@pytest.mark.asyncio
async def test_register_user(client):
    timestamp = int(time.time())
    email = f"user{timestamp}@teste.com"

    query = f"""
    mutation {{
      registerUser(email: "{email}", password: "123456") {{
        id
        email
      }}
    }}
    """
    response = await client.post("/graphql", json={"query": query})
    assert response.status_code == 200
    data = response.json()
    assert data["data"]["registerUser"]["email"] == email

@pytest.mark.asyncio
async def test_login_user(client):
    timestamp = int(time.time())
    email = f"userlogin{timestamp}@teste.com"

    # Primeiro registra
    register_query = f"""
    mutation {{
      registerUser(email: "{email}", password: "123456") {{
        id
        email
      }}
    }}
    """
    response = await client.post("/graphql", json={"query": register_query})
    assert response.status_code == 200

    # Faz login
    login_query = f"""
    mutation {{
      loginUser(email: "{email}", password: "123456") {{
        accessToken
        tokenType
      }}
    }}
    """
    response = await client.post("/graphql", json={"query": login_query})
    assert response.status_code == 200
    data = response.json()
    assert data["data"]["loginUser"]["tokenType"] == "bearer"
