from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Upload_File
from .forms import Upload_file
from django.contrib import messages
from django.core.mail import send_mail
from .handle_uploaded_file import handle_uploaded_file


# Create your views here.


# @login_required()
# def Upload(requsts):
#    #if requsts.method == 'POST':
#    form = Upload_file(requsts.POST or None)
#    if requsts.method == 'POST':
#        if form.is_valid():
#            form = Upload_file(requsts.POST, requsts.FILES)
#            new_item = form.save(commit=False)
#            new_item.user = requsts.user
#            new_item.save()
#            return redirect('article:index')
#    return render(requsts, 'File/Upload.html', {'form': form})

# @login_required()
# def Uploads(request):
#    form = Upload_file(request.POST or None)
#    if form.is_valid():
#        new_item = Upload_File(File=request.FILES)
#        new_item = form.save(commit=False)
#        new_item.user = request.user
#        new_item.save()
#        messages.success(request, 'your form upload successfully!!')
#        return redirect('article:index')
# else:
#    return render(request, 'File/Upload.html', {'form': form})
#    return render(request, 'File/Upload.html', {'form' : form})


def Show_Upload(request):
    post = Upload_File.objects.all()
    return render(request, 'File/Show.html', {'post': post})


@login_required()
def Upload(request):
    if request.method == 'POST':
        form = Upload_file(request.POST, request.FILES)
        if form.is_valid():
            new_item = Upload_File(File=request.FILES)
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'your form upload successfully!!')
            cd = form.cleaned_data
            subject = f"{cd['name']} project for this user {new_item.user} want you build website for him" \
                      f"{cd['name']} and this is BudgetAmount {cd['BudgetAmount']}"
            message = f"this is project name{Upload_File.name} for this user:{new_item.user} this is email for this " \
                      f"project and user{cd['email']} and this is url for example project{cd['example']}" \
                      f"this is file for this project{cd['File']} and this is phone number for user" \
                      f"{cd['phone_number']}"
            send_mail(subject,
                      message,
                      'sitemat8@gmail.com',
                      ['sitemat8@example.com'])

            return redirect('article:index')
    else:
        form = Upload_file()
    return render(request, 'File/Upload.html', {'form': form})
