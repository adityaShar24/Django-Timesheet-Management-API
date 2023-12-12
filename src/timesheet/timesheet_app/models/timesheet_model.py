from django.db import models
from django.contrib.auth.models import User
from .project_model import Project

class Timesheet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    hours_worked = models.DecimalField(max_digits=5, decimal_places=2)
    week_start_date = models.DateField()


    def __str__(self):
        return f"{self.user.username} - {self.project.project_name} - {self.week_start_date}"