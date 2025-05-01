from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class Car(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True, index=True)
    placa = Column(String, unique=True)
    marca = Column(String)
    modelo = Column(String)
    ano = Column(Integer)
    combustivel = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))