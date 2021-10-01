import json
import re

from django.urls import resolve, reverse
from rest_framework import response, status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from api.models import Pelicula, Personaje, Planeta




class TokenTestCase(APITestCase):

    def setUp(self):
        """Se crea el usuario para generar token"""
        self.user = User.objects.create_user(username='admin', password='root')


    def test_get_token(self):
        """Testea si devuelve un token para el usuario"""

        data = {"username": "admin", "password": "root"}
        response = self.client.post("/api-token-auth/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_un_authenticated(self):
        """En caso de no autenticarse"""
        self.client.force_authenticate(user=None)
        response = self.client.get("/api/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class PlanetaTestCase(APITestCase):

    url_planetas = '/api/planetas/'
    data_planetas = {
        "nombre": "Testworld",
        "diametro": 10000,
        "poblacion": 4000000
    }

    def setUp(self):
        """Set-up de un usuario para las peticiones"""
        self.user = User.objects.create_user(username='admin', password='root')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)


    def test_planetas_auth(self):
        """Estado del endpoint después de autenticarse el usuario"""
        response = self.client.get(self.url_planetas)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_planetas_post(self):
        """Evalúa si agrega nuevo elemento al modelo PLaneta"""

        response = self.client.post(self.url_planetas, self.data_planetas, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class PeliculaTestCase(APITestCase):


    url_peliculas = '/api/peliculas/'
    data_peliculas = {
        "titulo": "Titulo test",
        "texto_apertura": "Some text exampleeeeeee",
        "director": "Juan Camilo Villa",
        "productor": "Eric Satie",
        "planetas": PlanetaTestCase.data_planetas["nombre"]
    }

    def setUp(self):
        """Set-up de un usuario para las peticiones"""
        self.user = User.objects.create_user(username='admin', password='root')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)


    def test_peliculas_auth(self):
        """Estado del endpoint después de autenticarse el usuario"""
        response = self.client.get(self.url_peliculas)
        self.assertEqual(response.status_code, status.HTTP_200_OK)



class PersonajeTestCase(APITestCase):


    url_personaje = '/api/personajes/'
    data_personajes = {
        "nombre": "FooBar",
        "especie": "bit",
        "peliculas": PeliculaTestCase.data_peliculas["titulo"]
    }

    def setUp(self):
        """Set-up de un usuario para las peticiones"""
        self.user = User.objects.create_user(username='admin', password='root')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)


    def test_personajes_auth(self):
        """Estado del endpoint después de autenticarse el usuario"""
        response = self.client.get(self.url_personaje)
        self.assertEqual(response.status_code, status.HTTP_200_OK)