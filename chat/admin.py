from django.contrib import admin
from .models import Room,PrivRoom
#from django.contrib.auth.admin import UserAdmin
'''
class CustomRoom(admin.ModelAdmin):
    """Sets up the custom user admin display"""
    model = Room
    list_display=["id", "title", "staff_only"]
    list_display_links=["id", "title"]

class CustomPrivRoom(admin.ModelAdmin):
    """Sets up the custom user admin display"""
    model = PrivRoom
    list_display = ["id", "title", "private"]
    list_display_links=["id", "title"]

admin.site.register(CustomRoom, CustomPrivRoom)
'''
admin.site.register(
    Room,
    list_display=["id", "title", "staff_only"],
    list_display_links=["id", "title"],
)
admin.site.register(
    PrivRoom,
    list_display=["id", "title", "private"],
    list_display_links=["id", "title"],
)
