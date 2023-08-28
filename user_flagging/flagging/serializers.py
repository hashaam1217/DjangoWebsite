from rest_framework import serializers
from .models import Flag, Business, Customer 

class FlagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Business
        fields = "__all__"

class BusinessSerializer(serializers.ModelSerializer):

    class Meta:
        model = Business
        fields = "__all__"

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Business
        fields = "__all__"
