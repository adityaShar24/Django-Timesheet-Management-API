from rest_framework import serializers
from ..models.timesheet_model import Timesheet

class TimesheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timesheet
        fields = '__all__'
        
        
def validate(self, data):
    # Extract user and week_start_date from the input data
    user = data['user']
    week_start_date = data['week_start_date']

    # Retrieve the latest timesheet for the given user, ordered by week_start_date in descending order
    latest_timesheet = Timesheet.objects.filter(user=user).order_by('-week_start_date').first()

    # Check if there is a latest timesheet for the user
    if latest_timesheet:
        # Calculate the time difference between the current week_start_date and the latest timesheet's week_start_date
        time_difference = week_start_date - latest_timesheet.week_start_date

        # If the time difference is less than 7 days, raise a validation error
        if time_difference.days < 7:
            raise serializers.ValidationError("You can only create a timesheet after 6 days from your last timesheet.")

    # If all checks pass, return the original data
    return data
