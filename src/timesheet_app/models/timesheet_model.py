from django.db import models
from django.contrib.auth.models import User
from .project_model import Project

class Timesheet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    projects = models.ManyToManyField(Project)

    hours_worked = models.DecimalField(max_digits=5, decimal_places=2)

    week_start_date = models.DateField()

    def __str__(self):
        projects_str = ', '.join([str(project) for project in self.projects.all()])
        return f"{self.user.username} - {projects_str} - {self.week_start_date}"
