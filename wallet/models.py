from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField()


class Funds(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    current_blanace = models.IntegerField(default= 0 )
    previous_blanace = models.IntegerField(default= 0 )
    money_added = models.IntegerField(default = 0)
    money_removed = models.IntegerField(default= 0)

class Transacton(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    money_saving = models.IntegerField(default=0)
    money_spending = models.IntegerField(default= 0)
    time_of_transactiob = models.DateTimeField(timezone.now)

class Accounts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_name = models.CharField(max_length = 500)
    card_number = models.IntegerField(default= 0000000000000000)
    