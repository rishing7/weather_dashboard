from .views import index
from django.urls import path

urlpatterns = [
    path('info/', index, name='index'),
]
