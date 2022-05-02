from telnetlib import DO
from models.models import *
from rest_framework import serializers

class DogSerializer(serializers.ModelSerializer):
    class meta:
        model = Dog
        fields= '__all__'

class OwnerSerializer(serializers.ModelSerializer):
    class meta:
        model = Owner
        fields= '__all__'