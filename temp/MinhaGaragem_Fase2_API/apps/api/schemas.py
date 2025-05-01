import strawberry
from typing import List

@strawberry.type
class Car:
    id: int
    placa: str
    marca: str
    modelo: str
    ano: int
    combustivel: str

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Olá, mundo!"

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_car(self, placa: str, marca: str, modelo: str, ano: int, combustivel: str) -> Car:
        return Car(id=1, placa=placa, marca=marca, modelo=modelo, ano=ano, combustivel=combustivel)