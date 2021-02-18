from django.shortcuts import render

# Create your views here.


def Upload(requests):
    return render(requests, 'File/Form_requests.html')