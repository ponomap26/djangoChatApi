from django.contrib import admin



from ChatBec.models import Chat, Room, Profile


class RoomAdmin(admin.ModelAdmin):
    list_display = ("creater", 'name', "invited_user", "date")

    def invited_user(self, obj):
        return "\n".join([user.username for user in obj.invited.all()])

class ChatAdmin(admin.ModelAdmin):
    list_display = ("room", "user", "text", "date")

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'image']

admin.site.register(Chat, ChatAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Profile, ProfileAdmin)