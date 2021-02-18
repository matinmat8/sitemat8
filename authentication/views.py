from django.contrib.auth.models import UserManager, User
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import Sign_Up_Form


#def authentication(requsts):
#    username = username.POST


def mat(requests):
    return render(requests, 'authentication/mat.html')


def index(request):
    if request.method == 'POST':
        form = Sign_Up_Form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('article:index')

    else:
        form = Sign_Up_Form()
    return render(request, 'authentication/register.html', {
        'form': form
    })


def Login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('article/index')
    else:
        return render(request, 'authentication/error_login.html')