from django.urls import path
from ..views.project_view import create_project , get_project_detail , update_project_detail , get_projects


urlpatterns = [
    path('create' , create_project , name = 'create_project'),
    path('update/<str:pk>' , update_project_detail , name = 'update_project_detail'),
    path('list' , get_projects , name = 'get_all_project'),
    path('get_project_detail/<str:pk>' , get_project_detail , name = 'get_project_detail'),
]