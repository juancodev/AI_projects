from django.urls import path
from .views import hello
from .views import about


urlpatterns = [
    path("", hello),
    path("about/", about),
]
