from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from datetime import datetime

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField()


class Funds(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    current_balance = models.IntegerField(default= 0 )
    previous_balance = models.IntegerField(default= 0 )
    money_added = models.IntegerField(default = 0)
    money_removed = models.IntegerField(default= 0)

    def __str__(self):
        return self.user.email

class Transacton(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    money_saving = models.IntegerField(default=0)
    money_spending = models.IntegerField(default= 0)
    time_of_transaction = models.DateTimeField(default = datetime.now())

    def __str__(self):
        return self.user.email

class Accounts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_name = models.CharField(max_length = 500)
    card_number = models.IntegerField(default= 0000000000000000)
    