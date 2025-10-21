from django.shortcuts import render
from django.http import HttpResponse


# def home(request):
#     return render(request, "test.html")  # <-- use the exact filename

def home(request):
    return HttpResponse("Hello, world. You're at the polls page.")