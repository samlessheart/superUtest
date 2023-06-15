from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from api.serializer import  UserSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import parser_classes
from django.contrib.auth import get_user_model
User = get_user_model()





class AddUserView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        print(request.data)
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():        
            user = serializer.save()
            user.set_password(request.data['password'])
            user.save()
            
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



class UserDetailView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = self.request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def patch(self, request, format = None):   
        
        user = self.request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            if "password" in request.data.keys():
                user.set_password(request.data["password"])
                user.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        



