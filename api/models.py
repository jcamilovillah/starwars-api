from django.db import models


class Planeta(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=100)
    diametro = models.PositiveIntegerField(default=100)
    poblacion = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Planeta"
        ordering = ['nombre']

    def __str__(self):
        return f'Planeta {self.nombre}'


class Personaje(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    peliculas = models.ManyToManyField(
        'Pelicula', related_name="personaje_peliculas",
        default=[]
    )

    class Meta:
        verbose_name = "Personaje"
        ordering = ['nombre']

    def __str__(self):
        return f'{self.nombre}'


class Pelicula(models.Model):
    episodio = models.AutoField(primary_key=True, editable=False)
    titulo = models.CharField(max_length=200)
    texto_apertura = models.TextField(max_length=1000)
    director = models.CharField(max_length=120)
    productor = models.CharField(max_length=100)
    planetas = models.ManyToManyField(
        'Planeta', related_name="pelicula_planetas", verbose_name="Planetas"
    )

    class Meta:
        verbose_name = "Pelicula"
        ordering = ['episodio']

    def __str__(self):
        return f'{self.episodio}. {self.titulo}'
