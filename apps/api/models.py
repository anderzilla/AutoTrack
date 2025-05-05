from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# 🧑 Tabela de usuários
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    # Relacionamento 1-para-1 com UserProfile
    profile = relationship("UserProfile", back_populates="user", uselist=False)
    # Relacionamento 1-para-N com UserCar
    user_cars = relationship("UserCar", back_populates="user")


# 📄 Informações adicionais do usuário
class UserProfile(Base):
    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)

    nome = Column(String, nullable=False)
    data_nascimento = Column(Date, nullable=True)
    cep = Column(String, nullable=True)
    rua = Column(String, nullable=True)
    numero = Column(String, nullable=True)
    complemento = Column(String, nullable=True)
    cidade = Column(String, nullable=True)
    estado = Column(String, nullable=True)
    pais = Column(String, nullable=True)
    cpf = Column(String, unique=True, nullable=False)

    user = relationship("User", back_populates="profile")


# 🚗 Veículo
class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True)
    placa = Column(String, unique=True, nullable=False)
    chassi = Column(String, unique=True, nullable=False)
    marca = Column(String, nullable=False)
    modelo = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    cor = Column(String, nullable=True)
    cilindros = Column(Integer, nullable=True)
    combustivel = Column(String, nullable=False)
    categoria = Column(String, nullable=True)

    # Relacionamento com UserCar
    user_car = relationship("UserCar", back_populates="car", uselist=False)


# 🔗 Associação entre usuário e carro
class UserCar(Base):
    __tablename__ = "user_cars"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    car_id = Column(Integer, ForeignKey("cars.id"), unique=True, nullable=False)

    user = relationship("User", back_populates="user_cars")
    car = relationship("Car", back_populates="user_car")
