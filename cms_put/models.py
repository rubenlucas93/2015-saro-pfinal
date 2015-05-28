from django.contrib.auth.models   import User
from django.db                    import models


class Usuarios(models.Model):
    usuario     = models.CharField(max_length = 200)
    titulo      = models.CharField(max_length = 200)
    descripcion = models.CharField(max_length = 200)
    background  = models.CharField(max_length = 200)
    num = models.IntegerField()
    letra       = models.CharField(max_length = 200)
#AQUI HAY QUE MIRARLO BIEN, PORQUE NO SE DONDE SE hace el post DE CADA USUARIO, TITULO, LETRA, etc.

class Actividad(models.Model):
    tipo       = models.CharField(max_length = 500)
    titulo  = models.CharField(max_length = 500)
    gratuito  = models.BooleanField()
    duracion  = models.CharField(max_length=50)
    fecha = models.CharField(max_length=50)
    hora = models.CharField(max_length=50)
    FechaEleccion = models.CharField(max_length=50) #para anadir esto se busca, cuando se este guardando la actividad, en el POST la fecha de eleccion y se guarda haciendo algo asi como user.actividad_create(cosas..., FechaEleccion=...)
    URL      = models.CharField(max_length = 500)
    largaduracion = models.BooleanField()
    usuario=models.ForeignKey(Usuarios)
    numero=models.IntegerField()
    votacion=models.IntegerField()
    comentario=models.CharField(max_length = 500)
	#comentario = models.CharField(max_length = 500)
	#puntuacion = models.CharField(max_length = 500)
class database(models.Model):
    tipo       = models.CharField(max_length = 500)
    titulo  = models.CharField(max_length = 500)
    gratuito  = models.BooleanField()
    duracion  = models.CharField(max_length=40)
    fecha = models.CharField(max_length=40)
    hora = models.CharField(max_length=40)
    URL      = models.CharField(max_length = 500)
    largaduracion = models.BooleanField()
    numero= models.IntegerField()
    votacion=models.IntegerField()
    
class horaactualizacion(models.Model):
    hora=models.CharField(max_length=40)
    usuario=models.CharField(max_length=40)

	
