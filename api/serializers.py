from rest_framework import serializers
from restaurants.models import Restaurant

class RestaurantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
        	'name',
        	'opening_time',
        	'closing_time',
        	]

class RestaurantDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'owner', 'name', 'description', 'opening_time', 'closing_time']

class RestaurantUpdatelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'description', 'opening_time', 'closing_time']