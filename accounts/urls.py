from os import path

from django.urls import include

from .views import edit

urlpatterns = [

    path('accounts/edit/', edit, name='edit'),

]
