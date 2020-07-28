"""wallet_auth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .schema import schema
from graphene_django.views import GraphQLView
from graphql_jwt.decorators import jwt_cookie
from django.views.decorators.csrf import csrf_exempt
from wallet import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphiql/', jwt_cookie(GraphQLView.as_view(graphiql=True, schema=schema))),
    path('wallet/', include(urls)),
    path('paystack/', include(('paystack.urls','paystack'),namespace='paystack')),

    
]
