from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from ..serializers.timesheet_serializer import TimesheetSerializer

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_timesheet(request):
    response = None

    data = {
        "projects": request.data.get("projects"),
        "hours_worked": request.data.get("hours_worked"),
        "week_start_date": request.data.get("week_start_date"),
        "user": request.user.id
    }

    serializer = TimesheetSerializer(data= data)
    
    if serializer.is_valid():
        serializer.save()
        
        response_data = {
            "message": "Timesheet created successfully",
            "data": serializer.data
        }
        
        response = Response(response_data , status= HTTP_201_CREATED)
    else:
        response = Response(serializer.errors , status= HTTP_400_BAD_REQUEST)
        
    return response
    