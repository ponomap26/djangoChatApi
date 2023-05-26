from rest_framework import serializers
from django.contrib.auth.models import User

from ChatBec.models import Room, Chat

"""Сериализация пользователя"""


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


"""Сериализация комнат чата"""


class RoomSerializers(serializers.ModelSerializer):
    creater = UserSerializer()
    invited = UserSerializer(many=True)

    class Meta:
        model = Room
        fields = ("id", "creater", "invited", "date")


"""Сериализация чата"""


class ChatSerializers(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Chat
        fields = ("user", "text", "date")


"""Сериализация чата"""


class ChatPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ("room", "text")
