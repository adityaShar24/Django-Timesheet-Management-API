from django.urls import path
from .views.auth_view import register_user , login_user

urlpatterns = [
    path('auth/register/' , register_user , name='register_user'),
    path('auth/login/' , login_user , name='login_user' ),
] 