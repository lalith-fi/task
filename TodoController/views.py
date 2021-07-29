
from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import TodoitemSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import *
import jwt,datetime
from AuthController.models import User
from rest_framework import status

# Create your views here.

class getall_view(APIView):

    def get(self,request):
        #check whether any user is loggedin or not
        token=request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('please login')
        items=Todoitem.objects.all()
        serializer=TodoitemSerializer(items,many=True)
        return Response(serializer.data)

class getone_view(APIView):
    
    def get(self,request,id):

        #check whether any user is loggedin or not

        token=request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('please login')
        item=Todoitem.objects.get(id=id)
        serializer=TodoitemSerializer(item)
        return Response(serializer.data)

class create_view(APIView):
    def post(self,request):

        #check whether any user is loggedin or not

        token=request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('please login')

        # Decoding the token for checking whether it is user or admin

        payload=jwt.decode(token,'secrect', algorithms=["HS256"])
        
        user=User.objects.get(email=payload["email"])
        if user.role=="user":
            return Response(status=status.HTTP_401_UNAUTHORIZED)
            
        serializer=TodoitemSerializer(data=request.data)
        if not serializer.is_valid():
            return Response('Enter valid data')
        serializer.save()
        return Response(serializer.data)
class update_view(APIView):
    def put(self,request,id):

        #check whether any user is loggedin or not

        token=request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('please login')

        # Decoding the token for checking whether it is user or admin

        payload=jwt.decode(token,'secrect', algorithms=["HS256"])
        
        user=User.objects.get(email=payload["email"])
        if user.role=="user":
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        item=Todoitem.objects.get(id=id)                        # geting the todoitem using id and updating the todoitem with given data

        serializer=TodoitemSerializer(item,data=request.data) 
        if not serializer.is_valid():
            return Response('Enter valid data')
        serializer.save()
        return Response(serializer.data)

class delete_view(APIView):

    def delete(self,request,id):

        #checking whether any user is loggedin or not

        token=request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('please login')

        # Decoding the token for checking whether it is user or admin

        payload=jwt.decode(token,'secrect', algorithms=["HS256"])
        
        user=User.objects.get(email=payload["email"])
        if user.role=="user":
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        item=Todoitem.objects.get(id=id)
        item.delete()
        return Response('Record deleted successfully')