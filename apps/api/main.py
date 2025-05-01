import strawberry
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from strawberry.fastapi import GraphQLRouter
from sqlalchemy.orm import Session

from auth import verify_password, create_access_token, get_password_hash
from database import SessionLocal
from models import User
from schemas import Query, Mutation

app = FastAPI()

# Autenticação
@app.post("/register")
def register(form_data: OAuth2PasswordRequestForm = Depends()):
    db = SessionLocal()
    user = db.query(User).filter(User.email == form_data.username).first()
    if user:
        raise HTTPException(status_code=400, detail="Usuário já existe")
    hashed_password = get_password_hash(form_data.password)
    new_user = User(email=form_data.username, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    return {"msg": "Usuário criado"}

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    db = SessionLocal()
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Credenciais inválidas")
    token = create_access_token(data={"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}

# GraphQL
schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")