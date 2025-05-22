# AutoTrack 🚗

Sistema de gerenciamento de veículos pessoais com API moderna, autenticação e banco de dados relacional.  
Permite ao usuário registrar, visualizar e manter um histórico completo de seus carros.

---

## 🚀 Funcionalidades

- Registro e login de usuários com autenticação JWT
- Cadastro de perfis de usuário com:
  - Nome, data de nascimento, endereço completo (CEP, rua, número, complemento, cidade, estado e país) e CPF
- Cadastro de veículos com:
  - Placa, chassi, marca, modelo, ano, cor, cilindros, combustível, categoria
- Associação de veículos aos usuários
- Listagem de veículos e perfis
- API GraphQL moderna com Strawberry + FastAPI
- Banco de dados PostgreSQL gerenciado com SQLAlchemy e Alembic
- Testes automatizados com pytest e pytest-asyncio
- Ambiente completo containerizado com Docker

---

## 🛠️ Tecnologias utilizadas

- Python 3.11
- FastAPI
- Strawberry GraphQL
- PostgreSQL
- SQLAlchemy ORM
- Alembic
- Docker
- pgAdmin
- pytest + pytest-asyncio

---

## 🐳 Como rodar com Docker

1. Clone o repositório:

git clone https://github.com/anderzilla/AutoTrack.git
cd AutoTrack

2. Suba os containers:

docker-compose up --build

3. Acesse:

- GraphQL Playground: http://localhost:8000/graphql
- pgAdmin: http://localhost:5050
  - Usuário: admin@admin.com
  - Senha: admin

---

## 🔍 Estrutura atual

├── alembic/
├── alembic.ini
├── auth.py
├── database.py
├── Dockerfile
├── entrypoint.sh
├── main.py
├── models.py
├── requirements.txt
├── schemas.py
├── tests/
│   ├── conftest.py
│   ├── test_cars.py
│   ├── test_user_profiles.py
│   └── test_users.py
└── docker-compose.yml

---

## 🧪 Rodar os testes

docker-compose exec api pytest tests --asyncio-mode=auto

---

## 📌 Próximas etapas

- Proteger rotas GraphQL com JWT (em progresso)
- Implementar revisões, personalizações e ordens de serviço
- Criar queries públicas e privadas no GraphQL
- Desenvolver frontend com Next.js + Tailwind
- Desenvolver App Mobile com React Native (futuro)

---

## 👨‍💻 Autor

Desenvolvido por Anderson Henrique Gonçalves  
GitHub: https://github.com/anderzilla  
LinkedIn: https://www.linkedin.com/in/andersonhenriquegoncalves

---

## 📝 Licença

Este projeto está licenciado sob os termos da [MIT License](LICENSE).
