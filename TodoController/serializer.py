from django.db.models import fields
from rest_framework import serializers
from .models import *

class TodoitemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todoitem
        fields=['id','item']