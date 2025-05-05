import pytest
import time

@pytest.mark.asyncio
async def test_create_car(client):
    timestamp = int(time.time())
    email = f"usercar{timestamp}@teste.com"

    # Cria usuário
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
    user_data = response.json()
    user_id = user_data["data"]["registerUser"]["id"]

    # Cria carro (sem userId)
    car_query = f"""
    mutation {{
      createCar(
        placa: "TEST{timestamp}",
        chassi: "{timestamp}",
        marca: "Chevrolet",
        modelo: "Omega",
        ano: 1999,
        cor: "Preto",
        cilindros: 6,
        combustivel: "Gasolina",
        categoria: "Sedan"
      ) {{
        id
        placa
        marca
      }}
    }}
    """
    response = await client.post("/graphql", json={"query": car_query})
    assert response.status_code == 200
    data = response.json()
    assert data["data"]["createCar"]["placa"] == f"TEST{timestamp}"
