from django.contrib import admin
from .models.project_model import Project
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'user_id')

    def user_id(self, obj):
        return obj.id
    user_id.short_description = 'User ID'

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Project)
