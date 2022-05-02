from django.urls import path
from .views import *

urlpatterns = [
    path('', dog_list, name='index'),
]
