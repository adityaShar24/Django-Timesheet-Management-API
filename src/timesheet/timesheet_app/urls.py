from django.urls import path
from .views.auth_view import register_user

urlpatterns = [
    path('auth/register/' , register_user , name='register_user')
] 