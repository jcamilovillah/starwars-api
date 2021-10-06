# Star Wars API


API que permite ver información relacionada a la serie Star Wars, como personajes, planetas y películas.

## Instalación
#
Sigue los pasos a continuación para instalar el API:

```bash
git clone https://github.com/jcamilovillah/starwars-api.git
cd starwars-api

# Instalar los requerimientos
pip install -r requirements.txt

# Iniciar la base de datos y cargar los fixtures
python manage.py migrate

#Cargar los fixtures a la base de datos
python manage.py loaddata fixtures/*
```

Una vez esté todo hecho, arranca el servidor

```bash
python manage.py runserver
```


## Descripción de los endpoints
#

*Para facilitar los request según las condiciones, se debe usar la plataforma de consultas de API [Postman](https://www.postman.com/)*

* *POST* ```/api-token-auth/``` - Permite generar un token para que el usuario haga los request.

* *GET* ```/api/planetas/``` -  Retorna todas las instancias del modelo Planeta. Se puede filtrar la búsqueda por nombre, diámetro y población, colocándolos como argumento en la URL.

* *POST* ```/api/planetas/``` - Método para crear nuevas instancias del modelo Planeta. Recibe: nombre, diámetro y población.

* *GET* ```/api/peliculas/``` - Retorna todas las instancias del modelo Peliculas. Se puede filtrar la búsqueda por episodio y título, colocándolos como argumento en la URL.

* *POST* ```/api/peliculas/``` - Método para crear nuevas instancias del modelo Peliculas. Recibe: titulo, texto-apertura, director, productor y una lista de planetas, las cuales salen en la película.

* *GET* ```/api/personajes/``` - Retorna todas las instancias del modelo Personajes. Se puede filtrar la búsqueda por nombre y especie, colocándolos como argumento en la URL.

* *POST* ```/api/personajes/``` - Método para crear nuevas instancias del modelo Personajes. Recibe: nombre, especie y una lista de películas en las que sale el personaje.


## Cómo usar la API
#

### Generar el token:
Para poder usar la API, primero se debe generar un token para el usuario principal. Para ello, vamos a realizar un método *POST* al endpoint ```/api-token-auth/``` , pasando en fortamo en el *Body* en formato JSON las credenciales del usuario, las cuales están comentadas en el fichero ```settings.py```.  Al enviar la petición, el endpoint retornará el token, el cual se debe guardar para realizar consultas a la base de datos.


### Hacer una consulta:
Luego de obtener el token del usuario, ya estamos listos para poder hacer consultas o crear nuevos elementos.
Si lo que queremos es obtener datos acerca de un modelo como por ejemplo *Personaje* basta con apuntar a su enpoint ```/api/personajes/``` con el método *GET* y pasar el token en los *Headers*, con la *KEY*  ```Authorization``` y como *VALUE* `Token 'id-del-token-generado'`. Se envía la consulta con esas indicaciones y el endpoint retornará las instancias de Personaje.


### Añadir un nuevo elemento:
Para añadir ya se un nuevo personaje, planeta o película, es el mismo mecanismo que para obtenerlos, solo que con el método *POST*, es decir, se apunta al endpoint del modelo a añadir, y en *Body* se le pasarían los parámetros especificados arriba. Todo esto sin quitar el Header para la autenticación.

## Desarrollado por ✒️

<p align="left">
			<h3 align="left">Juan Camilo Villa H. </h3>
      		<p align="left">
	   		</a>
			<p align="left">
        <a href="https://twitter.com/jcamilovillah" target="_blank">
            <img alt="twitter_page" src="https://github.com/gedafu/readme-template/blob/master/images/twitter.png" style="float: center; margin-right: 10px" height="50" width="50">
        </a>
        <a href="https://www.linkedin.com/in/jcamilovillah/" target="_blank">
            <img alt="linkedin_page" src="https://github.com/gedafu/readme-template/blob/master/images/linkedin.png" style="float: center; margin-right: 10px" height="50"  width="50">
        </a>
        <a href="https://medium.com/@juancamilovilla" target="_blank">
            <img alt="medium_page" src="https://github.com/gedafu/readme-template/blob/master/images/medium.png" style="float: center; margin-right: 10px" height="50" width="50">
			 </a>
</p>

