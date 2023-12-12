from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from ..serializers.project_serializer import ProjectSerializer
from ..models.project_model import Project
from rest_framework.status import HTTP_200_OK , HTTP_400_BAD_REQUEST , HTTP_201_CREATED
from rest_framework.permissions import IsAuthenticated
from ..utils.constants import PROJECT_CREATED_MESSAGE , PROJECT_UPDATED_MESSAGE , ALL_PROJECTS_FETCHED_MESSAGE , DETAILED_PROJECTS_FETCHED_MESSAGE

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_project(request):
    response = None
    serializer = ProjectSerializer(data= request.data)

    if serializer.is_valid():
        serializer.save()
        
        response_data = {
            "message": PROJECT_CREATED_MESSAGE,
            "data": serializer.data
        }
        
        response = Response(response_data , status= HTTP_201_CREATED)
    else:
        response = Response(serializer.errors , status= HTTP_400_BAD_REQUEST)
    
    return response

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_project_detail(request , pk):
    response = None

    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(instance=project , data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        
        response_data = {
            "message": PROJECT_UPDATED_MESSAGE,
            "data": serializer.data
        }

        response =  Response(response_data , status= HTTP_201_CREATED)
    else:
        response = Response(serializer.errors , status= HTTP_400_BAD_REQUEST)
        
    return response
    
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_projects(request):
    response = None
    
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects , many=True)
    
    data = {
        "message": ALL_PROJECTS_FETCHED_MESSAGE,
        "data": serializer.data
    }
    
    response = Response(data , status= HTTP_200_OK )
    return response  


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_project_detail(request , pk):
    response = None
    
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(project)
    
    data = {
        "message": DETAILED_PROJECTS_FETCHED_MESSAGE,
        "data": serializer.data
    }
        
    response = Response(data , status = HTTP_200_OK )  

    return response    
