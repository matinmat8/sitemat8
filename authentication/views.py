from django.contrib.auth.models import UserManager, User
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm


#def authentication(requsts):
#    username = username.POST


def mat(requsts):
    return render(requsts, 'authentication/mat.html')


def index(requsts):
    if requsts.method == 'POST':
        form = UserCreationForm(requsts.POST)
        if form.is_valid():
            form.save()
            username = requsts.POST.form.cleaned_data.get('username')
            password = requsts.POST.form.cleaned_data.get('password')
            user = authenticate(requsts, username=username, password=password)
            login(requsts, user)
            return HttpResponseRedirect('home')

    else:
        form = UserCreationForm()
    return render(requsts, 'authentication/register.html', {
        'form': form
    })