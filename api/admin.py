from django.contrib import admin
from .models import *


@admin.register(Planeta)
class PlanetaAdmin(admin.ModelAdmin):
    pass


@admin.register(Personaje)
class PersonajeAdmin(admin.ModelAdmin):
    pass

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    pass
