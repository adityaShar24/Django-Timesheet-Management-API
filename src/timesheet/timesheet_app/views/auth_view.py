from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers.user_serializer import UserSerializer


@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.save()
        return Response(serializer.data , status=201)
    return Response(serializer.error_messages , status=400)
    