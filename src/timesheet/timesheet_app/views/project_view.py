from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers.project_serializer import ProjectSerializer

@api_view(['POST'])
def create_project(request):
    serializer = ProjectSerializer(data= request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data , status=201)
    return Response(serializer.error_messages , status= 400)

