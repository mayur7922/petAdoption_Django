from rest_framework.views import APIView #type: ignore
from rest_framework import generics, status #type: ignore
from rest_framework.response import Response #type: ignore
from rest_framework.permissions import IsAuthenticated #type: ignore
from .models import Pet
from .serializers import PetSerializer
from django.shortcuts import get_object_or_404 #type: ignore
from django.utils.decorators import method_decorator #type: ignore
from django.views.decorators.csrf import csrf_exempt #type: ignore

@method_decorator(csrf_exempt, name='dispatch')
class PetListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Pet.objects.all()
    serializer_class = PetSerializer

    def get(self, request, *args, **kwargs):
        pets = Pet.objects.all()
        serializer = PetSerializer(pets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = PetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class PetRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        pet_id = kwargs.get('id')
        pet = get_object_or_404(Pet, id=pet_id)
        serializer = PetSerializer(pet, data=request.data)
        return Response(serializer.initial_data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        pet_id = kwargs.get('id')
        pet = get_object_or_404(Pet, id=pet_id)
        serializer = PetSerializer(pet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        pet_id = kwargs.get('id')
        pet = get_object_or_404(Pet, id=pet_id)
        pet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@method_decorator(csrf_exempt, name='dispatch')
class RunningView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.username == "admin" and request.user.is_superuser:
            return Response({"message": "running"})
        return Response({"message": "Unauthorized"}, status=401)
