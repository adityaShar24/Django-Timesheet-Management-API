from rest_framework import serializers
from ..models.timesheet_model import Timesheet

class TimesheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timesheet
        fields = '__all__'
        
    def validate(self, data):
        user = data['user']
        week_start_date = data['week_start_date']

        latest_timesheet = Timesheet.objects.filter(user=user).order_by('-week_start_date').first()

        if latest_timesheet:
            time_difference = week_start_date - latest_timesheet.week_start_date
            if time_difference.days < 7:
                raise serializers.ValidationError("You can only create a timesheet after 6 days from your last timesheet.")

        return data