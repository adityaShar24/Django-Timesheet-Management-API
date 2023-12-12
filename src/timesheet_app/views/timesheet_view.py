from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK , HTTP_403_FORBIDDEN
from ..serializers.timesheet_serializer import TimesheetSerializer
from ..models.timesheet_model import Timesheet
from ..utils.constants import PERMISSION_DENIED_MESSAGE  , TIMESHEET_CREATED_SUCCESS_MESSAGE , TIMESHEET_UPDATE_SUCCESS_MESSAGE , ALL_TIMESHEETS_FETCHED_SUCCESS_MESSAGE , TIMESHEET_FETCHED_SUCCESS_MESSAGE

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
            "message": TIMESHEET_CREATED_SUCCESS_MESSAGE ,
            "data": serializer.data
        }
        
        response = Response(response_data , status= HTTP_201_CREATED)
    else:
        response = Response(serializer.errors , status= HTTP_400_BAD_REQUEST)
        
    return response


@api_view(["PUT"])
def update_timesheet(request , pk):
    response = None
    timesheet = Timesheet.objects.get(id= pk)

    if timesheet.user.id != request.user.id:
        response_data = {
            "message": PERMISSION_DENIED_MESSAGE
        }
        
        response = Response(response_data , status= HTTP_403_FORBIDDEN)
    else:
        data = {
            "projects": request.data.get("projects"),
            "hours_worked": request.data.get("hours_worked"),
            "week_start_date": request.data.get("week_start_date"),
            "user": request.user.id
        }
        
        serializer = TimesheetSerializer(instance= timesheet , data= data)
    
        if serializer.is_valid():
            serializer.save()
        
            response_data = { 
                "message": TIMESHEET_UPDATE_SUCCESS_MESSAGE ,
                "data": serializer.data
            }
        
            response = Response(response_data , status= HTTP_201_CREATED)
        else:
            response = Response(serializer.errors , status= HTTP_400_BAD_REQUEST)
        
    return response


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def list_all_timesheets(request):
    response = None

    timesheets = Timesheet.objects.filter(user= request.user.id)
    serializer = TimesheetSerializer(instance= timesheets , many=True)    
    
    data = {
        "message": ALL_TIMESHEETS_FETCHED_SUCCESS_MESSAGE,
        "data": serializer.data
    }
    
    response = Response(data , status= HTTP_200_OK)
    return response
    
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_by_id(request , pk):
    response = None
    
    timesheet = Timesheet.objects.get(id = pk)
    
    if timesheet.user.id != request.user.id:
        response = {
                "message": PERMISSION_DENIED_MESSAGE
            }
    else:
        serializer = TimesheetSerializer(instance= timesheet)
        
        data = {
            "message": TIMESHEET_FETCHED_SUCCESS_MESSAGE,
            "data": serializer.data
        }
        
        response = Response(data , status= HTTP_200_OK)

    return response
    