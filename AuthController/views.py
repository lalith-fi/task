
from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import UserSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import *
import jwt,datetime
# Create your views here.
class register_view(APIView):
    def post(self,request):
      serializer=UserSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
        serializer.save()
      return Response({'message':'Your account is registerd','Ur details':serializer.data})
    

class login_view(APIView):
    def post(self,request):
        email=request.data["email"]
        password=request.data["password"]
        user = User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('user not found')
        if not user.check_password(password):
            raise AuthenticationFailed('incorrect password')

        #encoding id,firstname,lastname,email,isactive,role and creating a jwt token

        payload={
        "id":user.id,
        "firstname":user.first_name,
        "lastname":user.last_name,
        "email":user.email,
        "isactive":user.is_active,
        "role":user.role,
        }
        token =jwt.encode(payload,"secrect",algorithm='HS256')

        # storing the token in the cookies

        response=Response()
        response.set_cookie(key="jwt" , value=token, httponly=True)
        response.data={"jwt" :token}
        return response
class logout_view(APIView):
    def get(self,request):
        response=Response()

        # deleting the token in the  cookies
         
        response.delete_cookie('jwt')
        response.data={
        "messsage " :"success"
        }
        return response