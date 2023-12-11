from django.urls import path
from .views.auth_view import register_user , login_user
from .views.project_view import create_project , update_project_detail , get_projects , get_project_detail

urlpatterns = [
    path('auth/register/' , register_user , name='register_user'),
    path('auth/login/' , login_user , name='login_user' ),
    path('project/create/' , create_project , name = 'create_project'),
    path('project/update/<str:pk>' , update_project_detail , name = 'update_project_detail'),
    path('project/get-all/' , get_projects , name = 'get_all_project'),
    path('project/get_project_detail/<str:pk>' , get_project_detail , name = 'get_project_detail'),
] 