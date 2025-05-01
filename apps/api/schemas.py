import strawberry
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from database import SessionLocal
from models import Car as CarModel, User as UserModel
from auth import get_password_hash, verify_password, create_access_token

@strawberry.type
class Car:
    id: int
    placa: str
    marca: str
    modelo: str
    ano: int
    combustivel: str

@strawberry.type
class User:
    id: int
    email: str

@strawberry.type
class AuthPayload:
    access_token: str
    token_type: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def to_car_type(car: CarModel) -> Car:
    return Car(
        id=car.id,
        placa=car.placa,
        marca=car.marca,
        modelo=car.modelo,
        ano=car.ano,
        combustivel=car.combustivel
    )

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Olá, mundo!"

    @strawberry.field
    def get_cars(self) -> List[Car]:
        try:
            db: Session = next(get_db())
            cars = db.query(CarModel).all()
            return [to_car_type(car) for car in cars]
        except Exception as e:
            raise Exception(f"Erro ao buscar carros: {str(e)}")

@strawberry.type
class Mutation:

    @strawberry.mutation
    def create_car(self, placa: str, marca: str, modelo: str, ano: int, combustivel: str) -> Car:
        db: Session = next(get_db())
        try:
            existing = db.query(CarModel).filter(CarModel.placa == placa).first()
            if existing:
                raise Exception(f"Já existe um carro com a placa {placa}.")
            new_car = CarModel(
                placa=placa,
                marca=marca,
                modelo=modelo,
                ano=ano,
                combustivel=combustivel,
                user_id=1
            )
            db.add(new_car)
            db.commit()
            db.refresh(new_car)
            return to_car_type(new_car)
        except IntegrityError:
            db.rollback()
            raise Exception("Erro de integridade ao cadastrar o carro.")
        except SQLAlchemyError as e:
            db.rollback()
            raise Exception(f"Erro ao salvar carro no banco de dados: {str(e)}")

    @strawberry.mutation
    def register_user(self, email: str, password: str) -> User:
        db: Session = next(get_db())
        try:
            if not email or not password:
                raise Exception("Email e senha são obrigatórios.")
            user = db.query(UserModel).filter(UserModel.email == email).first()
            if user:
                raise Exception("Email já registrado.")
            hashed_password = get_password_hash(password)
            new_user = UserModel(email=email, hashed_password=hashed_password)
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            return User(id=new_user.id, email=new_user.email)
        except IntegrityError:
            db.rollback()
            raise Exception("Erro de integridade ao registrar usuário.")
        except SQLAlchemyError as e:
            db.rollback()
            raise Exception(f"Erro ao registrar usuário: {str(e)}")

    @strawberry.mutation
    def login_user(self, email: str, password: str) -> AuthPayload:
        db: Session = next(get_db())
        try:
            if not email or not password:
                raise Exception("Email e senha são obrigatórios.")
            user = db.query(UserModel).filter(UserModel.email == email).first()
            if not user or not verify_password(password, user.hashed_password):
                raise Exception("Credenciais inválidas.")
            token = create_access_token(data={"sub": user.email})
            return AuthPayload(access_token=token, token_type="bearer")
        except Exception as e:
            raise Exception(f"Erro ao autenticar: {str(e)}")
