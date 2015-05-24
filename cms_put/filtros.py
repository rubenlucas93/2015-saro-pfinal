
import itertools
import urllib
import sys
from cms_put.models import Actividad, Usuarios, database, horaactualizacion
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding("utf-8")
#Hay que echarle un ojo a todos


def mostrartipo(filtro):

    lista = []
    LISTA = []

    DB = database.objects.all()
    lista=[]
    LISTA=[]
    for objeto in DB:
        
        LISTA.append(lista)
        lista=[]

        tipo=objeto.tipo
        titulo=objeto.titulo
        gratuito=objeto.gratuito
        fecha=objeto.fecha
        hora=objeto.hora
        largaduracion=objeto.largaduracion
        URL=objeto.URL
        duracion=objeto.duracion
        numero=objeto.numero
        print filtro
        print str(tipo)
        if str(tipo) == filtro:
            print 'entra'
            lista.append(objeto.tipo)
            lista.append(objeto.titulo)
            lista.append(objeto.gratuito)
            lista.append(objeto.fecha)
            lista.append(objeto.hora)
            lista.append(objeto.largaduracion)
            lista.append(objeto.URL)
            lista.append(objeto.duracion)
            lista.append(objeto.numero)
            
            LISTA.append(lista)
            lista = []
	
    return LISTA


def mostrargratuito(filtro):

    lista = []
    LISTA = []

    DB = database.objects.all()
    lista=[]
    LISTA=[]
    for objeto in DB:
        
        LISTA.append(lista)
        lista=[]

        tipo=objeto.tipo
        titulo=objeto.titulo
        gratuito=objeto.gratuito
        fecha=objeto.fecha
        hora=objeto.hora
        largaduracion=objeto.largaduracion
        URL=objeto.URL
        duracion=objeto.duracion
        numero=objeto.numero
        print gratuito
        print filtro
        if str(gratuito) == str(filtro):
            print 'entra'
            lista.append(objeto.tipo)
            lista.append(objeto.titulo)
            lista.append(objeto.gratuito)
            lista.append(objeto.fecha)
            lista.append(objeto.hora)
            lista.append(objeto.largaduracion)
            lista.append(objeto.URL)
            lista.append(objeto.duracion)
            lista.append(objeto.numero)
            
            LISTA.append(lista)
            lista = []
	
    return LISTA


def mostrarlargaduracion( filtro):
	
    
    lista = []
    LISTA = []

    DB = database.objects.all()
    lista=[]
    LISTA=[]
    for objeto in DB:
        
        LISTA.append(lista)
        lista=[]

        tipo=objeto.tipo
        titulo=objeto.titulo
        gratuito=objeto.gratuito
        fecha=objeto.fecha
        hora=objeto.hora
        largaduracion=objeto.largaduracion
        URL=objeto.URL
        duracion=objeto.duracion
        numero=objeto.numero
        if str(largaduracion) == str(filtro):
            lista.append(objeto.tipo)
            lista.append(objeto.titulo)
            lista.append(objeto.gratuito)
            lista.append(objeto.fecha)
            lista.append(objeto.hora)
            lista.append(objeto.largaduracion)
            lista.append(objeto.URL)
            lista.append(objeto.duracion)
            lista.append(objeto.numero)
            
            LISTA.append(lista)
            lista = []
	
    return LISTA

def mostrartitulo( filtro):

    
    lista = []
    LISTA = []

    DB = database.objects.all()
    lista=[]
    LISTA=[]
    for objeto in DB:
        
        LISTA.append(lista)
        lista=[]

        tipo=objeto.tipo
        titulo=objeto.titulo
        gratuito=objeto.gratuito
        fecha=objeto.fecha
        hora=objeto.hora
        largaduracion=objeto.largaduracion
        URL=objeto.URL
        duracion=objeto.duracion
        numero=objeto.numero
        if str(titulo) == str(filtro):
            lista.append(objeto.tipo)
            lista.append(objeto.titulo)
            lista.append(objeto.gratuito)
            lista.append(objeto.fecha)
            lista.append(objeto.hora)
            lista.append(objeto.largaduracion)
            lista.append(objeto.URL)
            lista.append(objeto.duracion)
            lista.append(objeto.numero)
            
            LISTA.append(lista)
            lista = []
	
    return LISTA


def mostrarfecha( filtro):
	
   
    lista = []
    LISTA = []

    DB = database.objects.all()
    lista=[]
    LISTA=[]
    for objeto in DB:
        
        LISTA.append(lista)
        lista=[]

        tipo=objeto.tipo
        titulo=objeto.titulo
        gratuito=objeto.gratuito
        fecha=objeto.fecha
        hora=objeto.hora
        largaduracion=objeto.largaduracion
        URL=objeto.URL
        duracion=objeto.duracion
        numero=objeto.numero

        if str(fecha) == str(filtro):

            lista.append(objeto.tipo)
            lista.append(objeto.titulo)
            lista.append(objeto.gratuito)
            lista.append(objeto.fecha)
            lista.append(objeto.hora)
            lista.append(objeto.largaduracion)
            lista.append(objeto.URL)
            lista.append(objeto.duracion)
            lista.append(objeto.numero)
            
            LISTA.append(lista)
            lista = []
	
    return LISTA


def mostrarhora( filtro):
	
    
    lista = []
    LISTA = []

    DB = database.objects.all()
    lista=[]
    LISTA=[]
    for objeto in DB:
        
        LISTA.append(lista)
        lista=[]

        tipo=objeto.tipo
        titulo=objeto.titulo
        gratuito=objeto.gratuito
        fecha=objeto.fecha
        hora=objeto.hora
        largaduracion=objeto.largaduracion
        URL=objeto.URL
        duracion=objeto.duracion
        numero=objeto.numero
        print gratuito
        print filtro
        if str(hora) == str(filtro):
            print 'entra'
            lista.append(objeto.tipo)
            lista.append(objeto.titulo)
            lista.append(objeto.gratuito)
            lista.append(objeto.fecha)
            lista.append(objeto.hora)
            lista.append(objeto.largaduracion)
            lista.append(objeto.URL)
            lista.append(objeto.duracion)
            lista.append(objeto.numero)
            
            LISTA.append(lista)
            lista = []
	
    return LISTA
