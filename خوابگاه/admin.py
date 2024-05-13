from django.contrib import admin
from .models import User
from .models import Room

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    fields = ('student_number', 'first_name', 'last_name', 'password', 'gender', 'phone')
    list_display = ('student_number', 'first_name', 'last_name', 'gender', 'phone')


class RoomAdmin(admin.ModelAdmin):
    fields = ('room_number', 'capacity', 'corridor', 'floor', 'dorm', 'is_full')
    list_display = ('room_number', 'capacity', 'corridor', 'floor', 'dorm', 'is_full')


admin.site.register(Room, RoomAdmin)
admin.site.register(User, UserAdmin)
