from django.contrib.auth import authenticate , logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers.user_serializer import UserSerializer
from ..serializers.login_serializer import LoginSerializer
from rest_framework.status import  HTTP_400_BAD_REQUEST , HTTP_201_CREATED , HTTP_200_OK , HTTP_401_UNAUTHORIZED
from rest_framework_simplejwt.tokens import RefreshToken , AccessToken
from ..utils.constants import USER_REGISTERED_MESSAGE , USER_LOGGEDIN_MESSAGE , INVAID_CREDENTIALS_MESSAGE , USER_LOGGEDOUT_MESSAGE , REFRESH_TOKEN_REQUIRED_MESSAGE

@api_view(['POST'])
def register_user(request):
    response = None
    
    serializer = UserSerializer(data = request.data)
    
    if serializer.is_valid(): 
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.save()
        
        response_data = {
            "message": USER_REGISTERED_MESSAGE ,
            "data" : serializer.data
        }
        
        response = Response( response_data , status= HTTP_201_CREATED)
    else:
        response = Response(serializer.errors , status= HTTP_400_BAD_REQUEST) 
    
    return response
    
    
@api_view(['POST'])
def login_user(request):
    response = None
    
    serializer = LoginSerializer(data = request.data)
    
    if serializer.is_valid():
        password = serializer.data['password']
        username = serializer.data['username']
        
        user = authenticate( request, username= username , password = password )
        
        if user is None:
            response = Response({"message": INVAID_CREDENTIALS_MESSAGE } , status= HTTP_400_BAD_REQUEST)
    
        refresh = RefreshToken.for_user(user)
        access = AccessToken.for_user(user)

        response =  Response(
            {
                'message': USER_LOGGEDIN_MESSAGE.format(username = username) ,
                'refresh': str(refresh),
                'access': str(access)
            }
        )
    
    else:
        response = Response( serializer.errors , status= HTTP_400_BAD_REQUEST)
        
    return response 
    

@api_view(['POST'])
def logout_user(request):
    response= None
    
    refresh_token= request.headers.get('refresh_token')

    if not refresh_token:
        response = Response({"message": REFRESH_TOKEN_REQUIRED_MESSAGE}, status= HTTP_401_UNAUTHORIZED)

    try:
        RefreshToken(refresh_token).blacklist()
        logout(request)
        response = Response({"message": USER_LOGGEDOUT_MESSAGE}, status= HTTP_200_OK)
    except Exception as e:
        response = Response({"error": str(e)}, status= HTTP_401_UNAUTHORIZED)
    return response