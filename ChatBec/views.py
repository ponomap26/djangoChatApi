from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import redirect, render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from django.contrib.auth.models import User

from ChatBec.forms import UserEditForm, ProfileEditForm
from ChatBec.models import Room, Chat, Profile
from ChatBec.serializers import (RoomSerializers, ChatSerializers, ChatPostSerializers, UserSerializer)

"""Комнаты чата"""


class Rooms(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        rooms = Room.objects.filter(Q(creater=request.user) | Q(invited=request.user))
        serializer = RoomSerializers(rooms, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        Room.objects.create(creater=request.user)
        return Response(status=201)


"""Диалог чата, сообщение"""


class Dialog(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        room = request.GET.get("room")
        chat = Chat.objects.filter(room=room)
        serializer = ChatSerializers(chat, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        dialog = ChatPostSerializers(data=request.data)
        if dialog.is_valid():
            dialog.save(user=request.user)
            return Response(status=201)
        else:
            return Response(status=400)


"""Добавление юзеров в комнату чата"""


class AddUsersRoom(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        room = request.data.get("room")
        user = request.data.get("user")
        try:
            room = Room.objects.get(id=room)
            room.invited.add(user)
            room.save()
            return Response(status=201)
        except:
            return Response(status=400)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)






@login_required
def edit(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)

    user_form = UserEditForm(instance=request.user)
    profile_form = ProfileEditForm(instance=profile)

    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('edit')

    return render(request, 'edit.html', {'user_form': user_form, 'profile_form': profile_form})


# """Регистрация пользователя"""
#
#
# class RegistrationAPIView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             # Create new user
#             user = User.objects.create(
#                 username=serializer.data['username'],
#                 email=serializer.data['email'])
#             user.set_password(serializer.data['password'])
#             user.save()
#             # Response with 201 Created status
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         # Response with 400 Bad Request status
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#
# """Авторизация пользователя"""
# class LoginAPIView(APIView):
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)
#
#     def post(self, request):
#         # получаем пользователя по переданным данным
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = User.objects.filter(username=username).first()
#         if not user or not user.check_password(password):
#             # сообщаем об ошибке
#             return Response({'error': 'Неверный логин или пароль'},
#                             status=status.HTTP_400_BAD_REQUEST)
#         # Генерируем новый токен для пользователя
#         token, created = Token.objects.get_or_create(user=user)
#         # Отправляем в ответе пользователю новый токен
#         return Response({'token': token.key})
