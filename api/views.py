from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Planeta, Personaje, Pelicula
from .serializers import PlanetaSerializer, PersonajeSerializer, PeliculaSerializer
from django_filters.rest_framework import DjangoFilterBackend

class PlanetaViewSet(viewsets.ModelViewSet):
    queryset = Planeta.objects.all()
    serializer_class = PlanetaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre', 'diametro', 'poblacion']

    def post(self, request):
        serializer = PlanetaSerializer(data=request.data)
        if serializer.is_valid():
            planeta = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['episodio', 'titulo']

    def post(self, request):
        serializer = PlanetaSerializer(data=request.data)
        if serializer.is_valid():
            planeta = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class PersonajeViewSet(viewsets.ModelViewSet):
    queryset = Personaje.objects.all()
    serializer_class = PersonajeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre', 'especie']

    def post(self, request):
        serializer = PlanetaSerializer(data=request.data)
        if serializer.is_valid():
            planeta = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
