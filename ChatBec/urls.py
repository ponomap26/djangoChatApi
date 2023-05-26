from django.template.defaulttags import url
from django.urls import path

from ChatBec import views
from ChatBec.views import *

urlpatterns = [
    path('room/', Rooms.as_view()),
    path('message/', Dialog.as_view()),
    path('users/', AddUsersRoom.as_view()),

]
