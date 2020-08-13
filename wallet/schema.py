import graphene
import graphql_jwt
from graphene_django import DjangoObjectType
from django.contrib.auth.models import User
from .models import Transacton, UserProfile, Accounts,Funds
# from .views import fund_wallet

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']

class FundWalletType(DjangoObjectType):
    class Meta:
        model = Funds
        fields = '__all__'

class TransactionType(DjangoObjectType):
    class Meta:
        model = Transacton
        fields = '__all__'


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
            user = User(first_name = first_name, last_name = last_name, email = email, username = email)
            user.set_password(password)
            user.save()
        return CreateUser(user = user)


class Fund_Wallet(graphene.Mutation):
      save_money = graphene.Field(FundWalletType)

      class Arguments:
          amount = graphene.String(required = True)
          

      def mutate(self, info, amount):
          amount = float(amount)
          user = info.context.user
          funds, funds_created = Funds.objects.get_or_create(user = user)
          transacton =  Transacton(user = user, money_saving = amount)
          funds.previous_balance = funds.current_balance
          funds.current_balance  = funds.current_balance + amount
          funds.money_added = amount
          funds.save()
          transacton.save()
          return Fund_Wallet(save_money = funds)
          


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    fund_Wallet = Fund_Wallet.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()

          

class Query:
    user = graphene.Field(UserType)
    funds = graphene.Field(FundWalletType)
    transactions = graphene.List(TransactionType)

    def resolve_user(self, info, **kwargs):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception('User not logged in')
        return user
    def resolve_funds(self, info, **kwargs):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception('No currently Logged in User')
        funds = Funds.objects.get(user = user)
        return funds
    def resolve_transactions(self, info, **kwargs):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception('No currently Logged in User')
        transactions = Transacton.objects.filter(user = user)
        return transactions

    

    

        