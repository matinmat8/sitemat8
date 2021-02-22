from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Upload_File
from .forms import Upload_file
from django.contrib import messages


# Create your views here.


#@login_required()
#def Upload(requsts):
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


def Upload(request):
    if request.method == 'POST':
        form = Upload_file(request.POST, request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            #new_item = Upload_file(file_fields=request.FILES)
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'your form upload successfully!!')
            return redirect('article:index')
    else:
        form = Upload_file()
        return render(request, 'File/Upload.html', {'form' : form})
