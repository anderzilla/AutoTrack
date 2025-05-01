import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

@strawberry.type
class Chama:
    @strawberry.field
    def hello(self) -> str:
        return "Olá, mundo!"


teste_query = Chama()
print(teste_query.hello())
schema = strawberry.Schema(query=Chama())
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
