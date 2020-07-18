import graphene
import graphql_jwt
from graphene_django import DjangoObjectType
from django.contrib.auth.models import User

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()

    class Arguments:
        first_name = graphene.String(required = True)
        last_name = graphene.String(required = True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, first_name, last_name, email, password):
        if User.objects.filter(email = email ).exists():
            raise Exception("Email already exists")
        else:
            user = User(first_name = first_name, last_name = last_name, email = email, username = " ")
            user.set_password(password)
            user.save()
        return CreateUser(user = user)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()

class Query:
    user = graphene.Field(UserType)

    def resolve_user(self, info, **kwargs):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception('Authentication credentials were not provided')
        return user
