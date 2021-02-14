from django.contrib.auth.models import UserManager
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
            objects = UserManager
            form.save()
            username = requsts.form.cleaned_data.get('username')
            password = requsts.form.cleaned_data.get('password')
            user = authenticate(requsts, username=username, password=password)
            login(requsts, user)
            return redirect('mat')

    else:
        form = UserCreationForm()
    return render(requsts, 'authentication/register.html', {
        'form': form
    })