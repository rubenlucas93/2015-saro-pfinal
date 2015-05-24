from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from cms_put.models import Actividad, Usuarios, database, horaactualizacion
from django.shortcuts import redirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.template import Template , Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from datetime import date
from django.db.models.base import ObjectDoesNotExist
from django.db import OperationalError

from cms_put.mostrar import guardaractividades, mostraractividades10, mostrarlista, sacaractividad
from cms_put.filtros import mostrartipo, mostrarfecha, mostrartitulo, mostrargratuito, mostrarlargaduracion, mostrarhora

import itertools
import urllib
import sys
import datetime
from bs4 import BeautifulSoup
#nota--> en vez de usar @csrf_exempt en todas las funciones, he comentado la linea correspondiente en settings
#mira a ver si eres capaz de modificar la variable   (en todas por ejemplo) para ver si se ha logeado desde admnin y que no haga falta que se logee desde la pagina de cultura (si da tiempo) algo asi como (si existe el usuario X guardalo en la base de datos)
reload(sys)
sys.setdefaultencoding("utf-8")



def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        try:        

            usuario = Usuarios.objects.get(usuario=username)

        except ObjectDoesNotExist:

            Usuarios(usuario=username, num= 1, titulo='usuario', descripcion='en madrid', background="white").save()
            horaactualizacion(hora='', usuario=username).save()
            
        print str(username)
        print str(password)
        if user:
            if user.is_active:
                login(request, user)
                 
                nombre = username
                

            return HttpResponseRedirect(('/Cultura/') + str(username))
        else:
            return HttpResponse('usuario incorrecto')

		
def logout_view(request):
    logout(request)
     
    nombre = ''

    return HttpResponseRedirect('/Cultura/')


def cambio(request):
    usuario  = str(request.user)
    usuario  = User.objects.get(username= usuario)
    password = str(request.POST['password'])
    usuario.set_password(password)
	
    pagina = ("<h1>cambiada correctamente.</h1>"
				"<form action='/cms_users/'method = 'GET'>"
				"<input type= 'submit' value='Index'></form>")
	
    return HttpResponse(pagina)


def principal(request):

    pagina="http://goo.gl/neEk0M"

    LISTA = mostraractividades10(pagina)
	

	
	########################################################################################################################
	#MOSTRAR PAGINAS PERSONALES
    DB = Usuarios.objects.all()
	
    l_usuario = []
    l_titulo = []
    l_descripcion = []
    l_id  = []
	
    for objeto in DB:
        l_usuario.append(objeto.usuario)
        l_titulo.append(objeto.titulo)
        l_descripcion.append(objeto.descripcion)
        l_id.append(objeto.id)
		
    print str(l_usuario)
	############################################################################################################################
	
    template=get_template('index.html')
    
    nombre=request.user.username
    if nombre=='':
        nombre='NO ESTAS REGISTRADO'
        BG="white"
    else:
        usuario=Usuarios.objects.get(usuario=nombre)
        BG=usuario.background 
    html = template.render(Context({'LISTA1' : l_usuario, 
                                    'LISTA2' : l_titulo,
                                    'LISTA3' : l_descripcion, 
                                    'LISTA4' : l_id,
                                    'FILA'   : LISTA,
                                    'USUARIO' : nombre,
                                    'TOPE'   : '10',
                                    'BG': BG}))
	
    return HttpResponse(html)

			
def todas(request):
	
    template=get_template('todas.html')
    pagina="http://goo.gl/neEk0M"
    LISTA=[]
	
    if request.method == 'POST':
        diccionario = request.POST
        lista       = list(diccionario.keys())
		

        


        if len(lista) != 0:

            columna = str(lista[0])
            print 'NAME: ' + columna
            filtrado = request.POST[columna]
			
            valor = str(filtrado)
            print 'VALUE: ' + valor

            if columna == 'seguir':
#valor es el identificador de la actividad que estas guardando
                actividad = sacaractividad(int(valor))
            

                 
                nombre=request.user.username
                print 'NOMBRE: ' + str(nombre)                
                try:                
                    usuario = Usuarios.objects.get(usuario = nombre)
                except ObjectDoesNotExist:
                    if str(nombre)!='':
                        usuario=Usuarios(usuario=nombre, num=1, background="white")
                        usuario.save()
                        horaactualizacion(hora='', usuario=nombre).save()
                    else:
                        return HttpResponse('no estas registrado')
                print usuario.id
                print actividad
                tipo=actividad[0]
                titulo=actividad[1]
                gratuito=actividad[2]
                
                fecha=actividad[3] 
                hora =actividad[4]
                URL=actividad[6]
                duracion=actividad[7]
                largaduracion=actividad[5]  
                FechaEleccion=str(datetime.datetime.now())
                usuario=usuario
                actividadnueva=Actividad(tipo=tipo, titulo=titulo, gratuito=gratuito, duracion=duracion, fecha=fecha, hora=hora, URL=URL, largaduracion=largaduracion, FechaEleccion=FechaEleccion, usuario=usuario)
                actividadnueva.save()
               
                
                


                
                

                

			###############################################################
			#FILTROS		
			
            if columna == 'titulo':
                print 'titulo'
                print 'titulo EN VIEWS: |' + str(valor)
                titulo = valor
                LISTA = mostrartitulo(titulo)

            elif columna == 'gratuito':
                print 'gratuito'
                print 'gratuito EN VIEWS: |' + str(valor)
                gratuito = valor
                if gratuito=="si":
                    gratuito="True"
                elif gratuito=="no":
                    gratuito="False"
                LISTA = mostrargratuito(gratuito)

            elif columna == 'largaduracion':
                print 'largaduracion'
                print 'largadiracopm EN VIEWS: |' + str(valor)
                largaduracion = valor
                if largaduracion=="si":
                    largaduracion="True"
                elif largaduracion=="no":
                    largaduracion="False"

                LISTA = mostrarlargaduracion(largaduracion)

            elif columna == 'fecha':
                print 'fecha'
                print 'fecha EN VIEWS: |' + str(valor)
                fecha = valor
                LISTA = mostrarfecha(fecha)

            elif columna == 'hora':
                print 'hora'
                print 'hora EN VIEWS: |' + str(valor)
                hora = valor
                LISTA = mostrarhora(hora)

            elif columna == 'tipo':
                print 'TIPO'
                print 'TIPO EN VIEWS: |' + str(valor)
                tipo = valor
                LISTA = mostrartipo(tipo)
            elif columna == 'actualizar':
                print 'actualizar'
                print 'actualizar EN VIEWS: |' + str(valor)
                pagina="http://goo.gl/neEk0M"
                DB=database.objects.all()
                LISTA=guardaractividades(pagina, DB)
                horaactual=datetime.datetime.now()
                hora=horaactualizacion.objects.get(usuario=request.user.username)
                print request.user.username
                print hora.usuario
                print horaactual
                hora.hora=horaactual
                hora.save()
            else:
                DB = database.objects.all()
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

    else:
  
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
            

    
	

    nombre=request.user.username
    if nombre == '':
        nombre = 'NO ESTAS REGISTRADO'
        horaactual=''
    try:
        print nombre
        hora=horaactualizacion.objects.get(usuario=nombre)
        horaactual=hora.hora
        print horaactual
    except ObjectDoesNotExist:
        horaactualizacion(hora='', usuario=request.user.username).save()
        horaactual=''
    try:
        usuario=Usuarios.objects.get(usuario=nombre)
    except ObjectDoesNotExist:
        if str(nombre)!='':
            usuario=Usuarios(usuario=nombre, num=1, titulo="usuario" ,descripcion="en madrid", background="white")
            usuario.save()
            horaactualizacion(hora='', usuario=nombre).save()

    html = template.render(Context({'TOPE'   : '10',
                                    'FILA'   : LISTA,
                                    'USUARIO' : nombre,
                                    'HORA':horaactual,                                  
                                    'BG': usuario.background,
                                    'LETRA': usuario.letra}))

    return HttpResponse(html)

						
def usuario(request, nombre):

    print 'USUARIO'
    print  nombre
    try:        

        usuario = Usuarios.objects.get(usuario=nombre)

    except ObjectDoesNotExist:

        return HttpResponse("el usuario " + str(nombre) + " no esta en nuestra base de datos. Pruebe a registrarse desde /Cultura/")
  
	
    if request.method == 'POST': #PARA CAMBIAR TITULO, DESCRIPCION, FONDO...

        diccionario = request.POST
        lista       = list(diccionario.keys())
	
        name = str(lista[0])
        valor = request.POST[name]

        print 'name:  ' + name
        print 'valor: ' + valor

        if name == 'titulo':
            usuario.titulo = (valor)
            usuario.save()
            titulo = valor
	
        if name == 'descripcion':
            usuario.descripcion = (valor)
            usuario.save()
            descripcion = valor

        if name == 'background':
            usuario.background = (valor)
            usuario.save()
            background = valor


	
        if name == 'letra':
            usuario.letra = (valor)
            usuario.save()
            letra = valor	
        if name == 'mas':
                usuario.num = usuario.num + 1
                usuario.save()
            
        if name == 'menos':
            if usuario.num>1:
                usuario.num = usuario.num - 1
                usuario.save()
                print usuario.num
                	
    template=get_template('usuario.html')

    lista=[]
    objeto=usuario.actividad_set.all()
    LISTA= mostrarlista(objeto)
    print len(LISTA)
    print usuario.num

    if len(LISTA)>(usuario.num)*8:
        lista=LISTA[((usuario.num-1)*8):((usuario.num)*8)]
    elif len(LISTA)>(usuario.num-1)*8 and len(LISTA)<(usuario.num)*8:
        lista=LISTA[((usuario.num-1)*8):-1]
    elif len(LISTA)<(usuario.num-1)*8:
        usuario.num=usuario.num-1
        usuario.save()   
        print usuario.num
    
    


    if nombre != '' :
        value = 0
    else:
    	value = 1

    html = template.render(Context({'USUARIO'         : nombre,
                                    'VALUE'       : value,
                                    'FILA'        : lista, 
                                    'TOPE'        : '10', 
                                    'DESCRIPCION' : usuario.descripcion, 
                                    'TITULO'      : usuario.titulo,
                                    'BG': usuario.background,

                                    'LETRA': usuario.letra})) 

    return HttpResponse(html)



def canalRSS (request, canal):
    print 'canalRSS'
    print 'CANAL RSS DE: ' + (canal)
	
    fichero  = open('actividades.xml')
    template = Template(fichero.read())
    fichero.close()
    
    usuarioCanal = canal
    usuario      = Usuarios.objects.get(usuario = usuarioCanal)
    objeto   = usuario.actividad_set.all()
	
    print objeto
    LISTA = []
    lista = []

    LISTA  = mostrarlista(objeto)
    
    FECHA = datetime.datetime.now()
	
    xml = template.render(Context({'USUARIO':usuarioCanal,
                                   'FILA' : LISTA,
								   'FECHA' : FECHA}))
	
    return HttpResponse(xml)

def ayuda (request):

    template=get_template('ayuda.html')
    html = template.render(Context({'TOPE'   : '10'}))
	

    return HttpResponse(html)

def actividad (request, indi):
    pagina="http://goo.gl/neEk0M"


    
    horaactual = datetime.datetime.now()
    lista= sacaractividad(indi)
   
    pagina=str(lista[6])
    pagina=urllib.urlopen(pagina)
    soup=BeautifulSoup(pagina)
#saco el primer trozo
    tag=list(soup.find_all("div"))

    for tag in tag:
        try:
            if str(tag["class"][0]).startswith("listadoInfo"):
                trozo2=tag.contents
        except KeyError:
            continue    
#de ahi saco el link en el que esta infoadicional
    try:
        soup=BeautifulSoup(str(trozo2))
        link=soup.find_all("a")[0]["href"]
    #lo analizo y saco la informacion que necesito
        pagina=urllib.urlopen("http://www.madrid.es" + str(link))
        soup=BeautifulSoup(pagina)
        tag=list(soup.find_all("div"))
        for tag in tag:
            try:
                if str(tag["class"][0]).startswith("tabContent"):
                    trozo3=tag.contents
            except KeyError:
                continue
        infoadicional=(str(trozo3[1]))
        infoadicional=Template(infoadicional)
        infoadicional=infoadicional.render(Context({'algo' : 1,}))
    except UnboundLocalError:
        infoadicional="no hay informacion adicional de este evento"
    except IndexError:
        infoadicional=str(trozo2[1])
        infoadicional=Template(infoadicional)
        infoadicional=infoadicional.render(Context({'algo' : 1,}))
    try:
        usuario=Usuarios.objects.get(usuario=request.user.username)
        BG=usuario.background 
    except ObjectDoesNotExist:
        BG="white"    
    template =get_template('actividades.html')
    html = template.render(Context({'INFO' : infoadicional,
                                    'HORA' : horaactual,
                                    'FILA'   : lista,
                                    'TOPE'   : '10',
                                    'BG': BG}))
	
    return HttpResponse(html)
    
    





