import xml.etree.cElementTree as etree
import itertools
import urllib
import sys
from bs4 import BeautifulSoup
from models import Actividad, database, Usuarios
from operator import itemgetter, attrgetter
from datetime import datetime
from django.db import OperationalError
reload(sys)
sys.setdefaultencoding("utf-8")

page="http://www.dgt.es/incidencias.xml"
def guardaractividades(page, DB): 
    feed = urllib.urlopen(page)
    soup = BeautifulSoup(feed)
    try:
        for elemento in DB:
            elemento.delete()
    except OperationalError:
        pass	

    lista = []
    LISTA = []
    contador = 1
    votacion=0

    actividades=soup.find_all("atributos")	

    for actividad in actividades:
        soup = BeautifulSoup(str(actividad))
        tag=soup.find_all("atributo")
        for tag in tag:
            if tag["nombre"]=="TIPO":
                tipo=str( tag.contents[0])
            if tag["nombre"]=="TITULO":
                titulo=str( tag.contents[0])
            if tag["nombre"]=="GRATUITO":
                gratuito=int( tag.contents[0])
            if tag["nombre"]=="FECHA-EVENTO":
                fecha=tag.contents[0]
                ano=int(str(fecha).split(" ")[0].split("-")[0])
                mes=int(str(fecha).split(" ")[0].split("-")[1])
                dia=int(str(fecha).split(" ")[0].split("-")[2])
                hora=int(str(fecha).split(" ")[1].split(".")[0].split(":")[0])
                minuto=int(str(fecha).split(" ")[1].split(".")[0].split(":")[1])
                segundo=int(str(fecha).split(" ")[1].split(".")[0].split(":")[2])
                fecha=datetime(ano, mes, dia, hora, minuto, segundo)
            if tag["nombre"]=="FECHA-FIN-EVENTO":
                fecha2=tag.contents[0]
                ano2=int(str(fecha2).split(" ")[0].split("-")[0])
                mes2=int(str(fecha2).split(" ")[0].split("-")[1])
                dia2=int(str(fecha2).split(" ")[0].split("-")[2])
                hora2=int(str(fecha2).split(" ")[1].split(".")[0].split(":")[0])
                minuto2=int(str(fecha2).split(" ")[1].split(".")[0].split(":")[1])
                segundo2=int(str(fecha2).split(" ")[1].split(".")[0].split(":")[2])
                fecha2=datetime(ano2, mes2, dia2, hora2, minuto2, segundo2)
                
                duracion=fecha2-fecha
                
            if tag["nombre"]=="HORA-EVENTO":
                hora=str( tag.contents[0])
            if tag["nombre"]=="EVENTO-LARGA-DURACION":
                largaduracion=int( tag.contents[0])
            if tag["nombre"]=="CONTENT-URL":
                URL=str( tag.contents[0])
        votaciones=Actividad.objects.filter(titulo=titulo, fecha=fecha)
        for objeto in votaciones:
            
            votacion = votacion + objeto.votacion



        lista.append(tipo)
        lista.append(titulo)
        lista.append(gratuito)
        lista.append(fecha)
        lista.append(hora)
        lista.append(largaduracion)
        lista.append(URL)
        lista.append(votacion)
        lista.append(duracion)

        lista.append(contador)

        database(tipo=tipo, titulo=titulo, gratuito=gratuito, fecha=str(fecha), hora=str(hora), largaduracion=largaduracion, URL=URL, duracion=str(duracion), votacion=votacion, numero=contador).save()
        contador = contador + 1

        LISTA.append(lista)
        lista = []

    return LISTA






def mostraractividades10(page):
	
    feed = urllib.urlopen(page)
    soup = BeautifulSoup(feed)

    lista = []
    LISTA = []

    contador = 1
    indice = 0
    actividades=list(soup.find_all("atributos"))
        

   
    hoy=datetime.now()
    ano=int(str(hoy).split(" ")[0].split("-")[0])
    mes=int(str(hoy).split(" ")[0].split("-")[1])
    dia=int(str(hoy).split(" ")[0].split("-")[2])
    hora=int(str(hoy).split(" ")[1].split(".")[0].split(":")[0])
    minuto=int(str(hoy).split(" ")[1].split(".")[0].split(":")[1])
    segundo=int(str(hoy).split(" ")[1].split(".")[0].split(":")[2])
    hoy=datetime(ano, mes, dia, hora, minuto, segundo)

    for actividad in actividades:
        soup = BeautifulSoup(str(actividad))
        tag=soup.find_all("atributo")
        
        for tag in tag:
            if tag["nombre"]=="TIPO":
                tipo=str( tag.contents[0])
            if tag["nombre"]=="TITULO":
                titulo=str( tag.contents[0])
            if tag["nombre"]=="GRATUITO":
                gratuito=int( tag.contents[0])
            if tag["nombre"]=="FECHA-EVENTO":
                fecha=tag.contents[0]
                ano=int(str(fecha).split(" ")[0].split("-")[0])
                mes=int(str(fecha).split(" ")[0].split("-")[1])
                dia=int(str(fecha).split(" ")[0].split("-")[2])
                hora=int(str(fecha).split(" ")[1].split(".")[0].split(":")[0])
                minuto=int(str(fecha).split(" ")[1].split(".")[0].split(":")[1])
                segundo=int(str(fecha).split(" ")[1].split(".")[0].split(":")[2])
                fecha=datetime(ano, mes, dia, hora, minuto, segundo)
            if tag["nombre"]=="FECHA-FIN-EVENTO":
                fecha2=tag.contents[0]
                ano=int(str(fecha2).split(" ")[0].split("-")[0])
                mes=int(str(fecha2).split(" ")[0].split("-")[1])
                dia=int(str(fecha2).split(" ")[0].split("-")[2])
                hora=int(str(fecha2).split(" ")[1].split(".")[0].split(":")[0])
                minuto=int(str(fecha2).split(" ")[1].split(".")[0].split(":")[1])
                segundo=int(str(fecha2).split(" ")[1].split(".")[0].split(":")[2])
                fecha2=datetime(ano, mes, dia, hora, minuto, segundo)
                
                duracion=fecha2-fecha
            if tag["nombre"]=="HORA-EVENTO":
                hora=str( tag.contents[0])
            if tag["nombre"]=="EVENTO-LARGA-DURACION":
                largaduracion=int( tag.contents[0])
            if tag["nombre"]=="CONTENT-URL":
                URL=str( tag.contents[0])
        
        if fecha<hoy: 
            indice=indice+1
        lista.append(tipo)
        lista.append(titulo)
        lista.append(gratuito)
        lista.append(str(fecha))
        lista.append(str(hora))
        lista.append(largaduracion)
        lista.append(URL)
        lista.append(str(duracion))
        

    

        lista.append(contador)

        contador=contador+1
        LISTA.append(lista)
        lista = []

    actividadesordenadas=sorted(LISTA, key=itemgetter(3,4))

               
        #esto es para que sean fechas posteriores a hoy
             
      

    actividades10=actividadesordenadas[indice:indice+9]
			
    return actividades10

def mostrarlista(DB):
	
    LISTA = []
    lista = []

    if DB != '':
        try:
            for objeto in DB:
                    print 'cacahuete'
                    lista.append(objeto.tipo)
                    lista.append(objeto.titulo)
                    lista.append(objeto.gratuito)
                    lista.append(objeto.duracion)
                    lista.append(objeto.fecha)
                    lista.append(objeto.hora)
                    lista.append(objeto.largaduracion)
                    try:
                        lista.append(objeto.FechaEleccion)
                    except AttributeError:
                        pass
                    lista.append(objeto.URL)
                    lista.append(objeto.votacion)
                    lista.append(objeto.numero)

                    LISTA.append(lista)
                    print lista
                    lista = []
        except OperationalError:
            pass
    print len(LISTA)
            
    return LISTA
	

	
def sacaractividad(iteracion): 
    
    lista    = []

    
            
    DB = database.objects.all()
    print len(DB)
    lista=[]
    LISTA=[]
    for objeto in DB:
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
        lista=[]
        
    actividadout = LISTA[int(iteracion)-1]
            
    print actividadout[4]
    print str(actividadout[4])
            
    return actividadout
	

	
	
	
	
	
	
	
	
	
	
	
	
	
