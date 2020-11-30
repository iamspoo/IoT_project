from rest_framework import serializers
from .models import light

class ModeSerializer(serializers.ModelSerializer):
    class Meta:
        model=light
        fields=['mode']

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model=light
        fields=['status']
        