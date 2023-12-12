from django.urls import path
from ..views.timesheet_view import create_timesheet , update_timesheet


urlpatterns = [
    path('create' , create_timesheet , name='create_timesheet'),
    path('update/<str:pk>' , update_timesheet , name='update_timesheet'),
]