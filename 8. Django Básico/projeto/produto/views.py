from django.shortcuts import render
from django.http import HttpResponse


def metodo(request):
    return render(request, 'produto/index.html')
