import graphene
import graphql_jwt
from graphene_django import DjangoObjectType
from django.contrib.auth.models import User
from .models import Transaction, UserProfile, Accounts,Funds
from datetime import datetime
import pytz
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
        model = Transaction
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
          time_of_transaction = graphene.String(required = True)
          

      def mutate(self, info, amount, time_of_transaction):
          amount = float(amount)
          user = info.context.user
          funds, funds_created = Funds.objects.get_or_create(user = user)
          date = time_of_transaction.split(',')[0]
          time = time_of_transaction.split(',')[1].split(' ')[0]
          month,day, year =int(date.split('/')[0]), int(date.split('/')[1]), int(date.split('/')[2])
          hour, minute, second = int(time.split(':')[0]), int(time.split(':')[1]), int(time.split(':')[2])
          d = datetime(year, month, day, hour, minute,second, tzinfo=pytz.UTC)
          transaction =  Transaction(user = user, money_saving = amount, time_of_transaction = d)
          funds.previous_balance = funds.current_balance
          funds.current_balance  = funds.current_balance + amount
          funds.money_added = amount
          funds.save()
          transaction.save()
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
        transactions = Transaction.objects.filter(user = user).order_by('-id')
        return transactions

    

    

        