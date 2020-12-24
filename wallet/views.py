from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fund_wallet(request, amount):
    pass

def verify_email(request):
    print(request.route)
    return HttpResponse("<html><body>It is now %s.</body></html>")