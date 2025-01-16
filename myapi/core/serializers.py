from rest_framework import serializers #type: ignore
from .models import Pet

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ["id", "type", "breed", "age", "isAdopted", "user_id"]