import strawberry
from typing import List
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Car as CarModel, User as UserModel, UserProfile as UserProfileModel, UserCar
from auth import get_password_hash, verify_password, create_access_token
import datetime

@strawberry.type
class Car:
    id: int
    placa: str
    chassi: str
    marca: str
    modelo: str
    ano: int
    cor: str
    cilindros: int
    combustivel: str
    categoria: str

@strawberry.type
class User:
    id: int
    email: str

@strawberry.type
class UserProfile:
    id: int
    nome: str
    data_nascimento: str
    cep: str
    rua: str
    numero: str
    complemento: str
    cidade: str
    estado: str
    pais: str
    cpf: str

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
        chassi=car.chassi,
        marca=car.marca,
        modelo=car.modelo,
        ano=car.ano,
        cor=car.cor,
        cilindros=car.cilindros,
        combustivel=car.combustivel,
        categoria=car.categoria
    )

def to_user_profile_type(profile: UserProfileModel) -> UserProfile:
    return UserProfile(
        id=profile.id,
        nome=profile.nome,
        data_nascimento=str(profile.data_nascimento),
        cep=profile.cep,
        rua=profile.rua,
        numero=profile.numero,
        complemento=profile.complemento,
        cidade=profile.cidade,
        estado=profile.estado,
        pais=profile.pais,
        cpf=profile.cpf
    )

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Olá, mundo!"

    @strawberry.field
    def get_cars(self) -> List[Car]:
        db: Session = next(get_db())
        cars = db.query(CarModel).all()
        return [to_car_type(car) for car in cars]

@strawberry.type
class Mutation:
    @strawberry.mutation
    def register_user(self, email: str, password: str) -> User:
        db = next(get_db())
        user = db.query(UserModel).filter(UserModel.email == email).first()
        if user:
            raise Exception("Email já registrado.")
        hashed_password = get_password_hash(password)
        new_user = UserModel(email=email, hashed_password=hashed_password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return User(id=new_user.id, email=new_user.email)

    @strawberry.mutation
    def login_user(self, email: str, password: str) -> AuthPayload:
        db = next(get_db())
        user = db.query(UserModel).filter(UserModel.email == email).first()
        if not user or not verify_password(password, user.hashed_password):
            raise Exception("Credenciais inválidas.")
        token = create_access_token(data={"sub": user.email})
        return AuthPayload(access_token=token, token_type="bearer")

    @strawberry.mutation
    def create_user_profile(
        self,
        user_id: int,
        nome: str,
        data_nascimento: str,
        cep: str,
        rua: str,
        numero: str,
        complemento: str,
        cidade: str,
        estado: str,
        pais: str,
        cpf: str
    ) -> UserProfile:
        db = next(get_db())
        existing_profile = db.query(UserProfileModel).filter(UserProfileModel.user_id == user_id).first()
        if existing_profile:
            raise Exception("Perfil já existente para esse usuário.")
        new_profile = UserProfileModel(
            user_id=user_id,
            nome=nome,
            data_nascimento=datetime.datetime.strptime(data_nascimento, "%Y-%m-%d").date(),
            cep=cep,
            rua=rua,
            numero=numero,
            complemento=complemento,
            cidade=cidade,
            estado=estado,
            pais=pais,
            cpf=cpf
        )
        db.add(new_profile)
        db.commit()
        db.refresh(new_profile)
        return to_user_profile_type(new_profile)

    @strawberry.mutation
    def create_car(
        self,
        placa: str,
        chassi: str,
        marca: str,
        modelo: str,
        ano: int,
        cor: str,
        cilindros: int,
        combustivel: str,
        categoria: str
    ) -> Car:
        db: Session = next(get_db())

        # Cria o carro
        new_car = CarModel(
            placa=placa,
            chassi=chassi,
            marca=marca,
            modelo=modelo,
            ano=ano,
            cor=cor,
            cilindros=cilindros,
            combustivel=combustivel,
            categoria=categoria
        )
        db.add(new_car)
        db.commit()
        db.refresh(new_car)

        # Pega o primeiro usuário (ideal para testes, no futuro pegaremos do token JWT)
        user = db.query(UserModel).first()
        if not user:
            raise Exception("Nenhum usuário encontrado para vincular ao carro.")

        user_car = UserCar(user_id=user.id, car_id=new_car.id)
        db.add(user_car)
        db.commit()

        return to_car_type(new_car)
