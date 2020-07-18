import graphene
from wallet.schema import Mutation as userMutation
from wallet.schema import Query as userQuery
class Query(userQuery, graphene.ObjectType):
    pass

class Mutation(userMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query = Query, mutation=Mutation)