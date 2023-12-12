from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/project/' , include("timesheet_app.urls.project_urls")),
    path('api/auth/' , include("timesheet_app.urls.auth_urls")),
    path('api/timesheet/' , include("timesheet_app.urls.timesheet_urls")),
]
