from django.contrib import admin
from .models import *

@admin.register(Userinfo)
class UserinfoAdmin(admin.ModelAdmin):
    list_display = ["id","username","gender",]
    list_filter = ["id","username","gender"]
    list_per_page = 10
    list_display_links = ["username"]

