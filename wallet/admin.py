from django.contrib import admin
from .models import Transaction,  Accounts,Funds
# Register your models here.
admin.site.register(Transaction)
admin.site.register(Accounts)
admin.site.register(Funds)
