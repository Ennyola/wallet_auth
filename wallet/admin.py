from django.contrib import admin
from .models import Transacton, UserProfile, Accounts,Funds
# Register your models here.
admin.site.register(Transacton)
admin.site.register(UserProfile)
admin.site.register(Accounts)
admin.site.register(Funds)
