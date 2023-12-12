from django.urls import path
from ..views.timesheet_view import create_timesheet , update_timesheet , list_all_timesheets , get_by_id


urlpatterns = [
    path('create' , create_timesheet , name='create_timesheet'),
    path('update/<str:pk>' , update_timesheet , name='update_timesheet'),
    path('list' , list_all_timesheets , name='list_all_timesheets'),
    path('get/<str:pk>' , get_by_id , name='get_by_id'),
]