from django.urls import path
from .views import log_hello

urlpatterns = [
    path("hello/", log_hello),
]
