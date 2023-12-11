from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers.project_serializer import ProjectSerializer
from ..models.project_model import Project

@api_view(['POST'])
def create_project(request):
    serializer = ProjectSerializer(data= request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data , status=201)
    return Response(serializer.error_messages , status= 400)

@api_view(["PUT"])
def update_project(request , pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(instance=project , data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data , status=201)
    
