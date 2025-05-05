import pytest
import time

@pytest.mark.asyncio
async def test_create_user_profile(client):
    # Gera um email único com timestamp
    timestamp = int(time.time())
    email = f"profile{timestamp}@teste.com"

    # Primeiro cria um usuário
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

    # Agora cria o profile com esse user_id
    profile_query = f"""
    mutation {{
      createUserProfile(
        userId: {user_id},
        nome: "Anderson Henrique",
        dataNascimento: "1980-05-05",
        cep: "80000-000",
        rua: "Rua Exemplo",
        numero: "123",
        complemento: "Apto 45",
        cidade: "Curitiba",
        estado: "PR",
        pais: "Brasil",
        cpf: "{timestamp}"  # CPF também único no teste para não dar conflito
      ) {{
        id
        nome
        cidade
      }}
    }}
    """
    response = await client.post("/graphql", json={"query": profile_query})
    assert response.status_code == 200
    data = response.json()
    assert data["data"]["createUserProfile"]["nome"] == "Anderson Henrique"
