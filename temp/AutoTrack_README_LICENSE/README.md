# AutoTrack 🚗

Sistema de gerenciamento de veículos pessoais com API moderna, autenticação e banco de dados relacional.  
Permite ao usuário registrar, visualizar e manter um histórico completo de seus carros.

---

## 🚀 Funcionalidades

- Registro e login de usuários com autenticação JWT
- Cadastro de veículos com:
  - Placa, marca, modelo, ano e combustível
- Listagem de todos os veículos cadastrados
- API GraphQL moderna com Strawberry + FastAPI
- Banco de dados PostgreSQL gerenciado com SQLAlchemy e Alembic
- Ambiente completo containerizado com Docker

---

## 🛠️ Tecnologias utilizadas

- [Python 3.11](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Strawberry GraphQL](https://strawberry.rocks/)
- [PostgreSQL](https://www.postgresql.org/)
- [SQLAlchemy ORM](https://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [Docker](https://www.docker.com/)
- [pgAdmin](https://www.pgadmin.org/) para administração do banco

---

## 🐳 Como rodar com Docker

### 1. Clone o repositório

```bash
git clone https://github.com/anderzilla/AutoTrack.git
cd AutoTrack
```

### 2. Suba os containers com Docker Compose

```bash
docker-compose up --build
```

### 3. Acesse os serviços:

- **GraphQL Playground:** [http://localhost:8000/graphql](http://localhost:8000/graphql)
- **pgAdmin (banco):** [http://localhost:5050](http://localhost:5050)
  - Usuário: `admin@admin.com`
  - Senha: `admin`

---

## 📦 Estrutura atual

```
apps/
  api/
    ├── main.py
    ├── models.py
    ├── schemas.py
    ├── auth.py
    ├── database.py
    ├── requirements.txt
    └── alembic/
docker-compose.yml
README.md
```

---

## 📌 Próximas etapas

- Proteger rotas GraphQL com JWT
- Implementar revisões, personalizações e ordens de serviço
- Desenvolver frontend com Next.js + Tailwind

---

## 👨‍💻 Autor

Desenvolvido por **Anderson Henrique Gonçalves**  
[GitHub](https://github.com/anderzilla) • [LinkedIn](https://www.linkedin.com/in/andersonhg)

---

## 📝 Licença

Este projeto está licenciado sob os termos da [MIT License](LICENSE).
