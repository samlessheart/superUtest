from rest_framework import serializers, status
from main.models import *
from django.contrib.auth import get_user_model


User = get_user_model()



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'bio', 'password', 'picture']
        extra_kwargs = {
            'password': {'write_only': True},
           
        }




