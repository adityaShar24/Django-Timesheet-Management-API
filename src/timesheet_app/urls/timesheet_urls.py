from django.urls import path
from ..views.timesheet_view import create_timesheet


urlpatterns = [
    path('create' , create_timesheet , name='create_timesheet'),
]