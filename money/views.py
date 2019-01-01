from django.shortcuts import render
from django.http import HttpResponse
from .models import Wallet, Category, Transaction

user = None
def base_generic(request):
    #return 0 cac ham lien ket trong url phai tra ve httpresponse 
    return render(request, 'money/transactions.html',)
def register(request):
    return render(request, 'registration/register.html')

from django.contrib.auth.models import User
from django.db import IntegrityError
import logging
def create_account(request):
    username = request.POST['username']#neu dung id cua label thi: request.POST.get('usernemr', False)
    password = request.POST['password']
    try:
        user = User.objects.create_user(username=username, password=password)
        message = 'successfully!'
        logger.info(message)
        return render(request, 'registration/register.html')
    except (IntegrityError): 
        message = 'account existed!'
        #logger.info(message)
        return render(request, 'registration/login.html')

from django.contrib.auth import authenticate, login
def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        #print("user id = "+str(user.id))
        # Redirect to a success page.
        return render(request, 'login_view.html')
    else:
        # Return an 'invalid login' error message.
        return render(request, 'registration/login.html')
    
"""def add_wallet(request,)
    
def add_transaction(request,)
    
def aad_category(request,)"""
    
from django.contrib.auth import logout
def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return render(request, 'registration/logged_out.html')