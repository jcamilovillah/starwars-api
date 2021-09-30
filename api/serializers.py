from rest_framework import serializers
from .models import Planeta, Personaje, Pelicula


class PlanetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planeta
        fields = '__all__'

    def create(self, validated_data):
        instance = Planeta()
        instance.nombre = validated_data.get('nombre')
        instance.diametro = validated_data.get('diametro')
        instance.poblacion = validated_data.get('poblacion')

        instance.save()

        return instance


class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = '__all__'

    planetas = PlanetaSerializer(many=True)

    def create(self, validated_data):
        instance = Pelicula()
        instance.titulo = validated_data.get('nombre')
        instance.texto_apertura = validated_data.get('texto_apertura')
        instance.director = validated_data.get('director')
        instance.productor = validated_data.get('productor')
        instance.planetas.set(validated_data.get('planetas'))

        instance.save()

        return instance


class PersonajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personaje
        fields = '__all__'
    
    peliculas = PeliculaSerializer(many=True)

    def create(self, validated_data):
        instance = Personaje()
        instance.id = validated_data.get('id')
        instance.nombre = validated_data.get('nombre')
        instance.especie = validated_data.get('especie')

        instance.save()

        return instance
