from django.shortcuts import render
from django.http import HttpResponse


def log_hello(request):
    return HttpResponse("Hello")
