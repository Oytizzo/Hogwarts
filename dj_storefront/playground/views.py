from django.http import HttpResponse
from django.shortcuts import render


def hello_world(request):
    x = 1
    y = 2
    sum = x + y
    return render(request, "hello.html", {})
