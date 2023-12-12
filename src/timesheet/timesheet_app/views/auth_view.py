from django.contrib.auth import authenticate , logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers.user_serializer import UserSerializer
from ..serializers.login_serializer import LoginSerializer
from rest_framework.status import  HTTP_400_BAD_REQUEST , HTTP_201_CREATED , HTTP_200_OK , HTTP_401_UNAUTHORIZED
from rest_framework_simplejwt.tokens import RefreshToken , AccessToken
from ..utils.constants import USER_REGISTERED_MESSAGE , USER_LOGGEDIN_MESSAGE , INVAID_CREDENTIALS_MESSAGE , USER_LOGGEDOUT_MESSAGE

@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data = request.data)
    
    if serializer.is_valid(raise_exception=True): 
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.save()
        
        response_data = {
            "message": USER_REGISTERED_MESSAGE ,
            "data" : serializer.data
        }
        
        return Response( response_data , status= HTTP_201_CREATED)
    
    return Response(serializer.errors , status= HTTP_400_BAD_REQUEST)
    
    
@api_view(['POST'])
def login_user(request):
    serializer = LoginSerializer(data = request.data)
    
    if serializer.is_valid(raise_exception=True):
        password = serializer.data['password']
        username = serializer.data['username']
        
        user = authenticate( request, username= username , password = password )
        
        if user is None:
            return Response({"message": INVAID_CREDENTIALS_MESSAGE } , status= HTTP_400_BAD_REQUEST)
    
        refresh = RefreshToken.for_user(user)
        access = AccessToken.for_user(user)

        return Response(
            {
                'message': USER_LOGGEDIN_MESSAGE.format(username = username) ,
                'refresh': str(refresh),
                'access': str(access)
            }
        )
    
    return Response( serializer.errors , status= HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def logout_user(request):
    refresh_token = request.data.get('refresh_token')

    if not refresh_token:
        return Response({"error": "Refresh token is required."}, status= HTTP_401_UNAUTHORIZED)

    try:
        RefreshToken(refresh_token).blacklist()
        logout(request)
        return Response({"message": USER_LOGGEDOUT_MESSAGE}, status= HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status= HTTP_401_UNAUTHORIZED)