from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product


def log_hello(request):
    # return HttpResponse("Hello")
    query_set = Product.objects.all()
    return render(request, "hello.html", {"products": query_set})
