from django.shortcuts import render


def home(request):
    return render(request, "test.html")  # <-- use the exact filename
