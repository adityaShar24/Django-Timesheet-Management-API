from rest_framework import serializers
from ..models.timesheet_model import Timesheet

class TimesheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timesheet
        fields = '__all__'