from django.shortcuts import render
from django.core.urlresolvers import reverse 
from django.http import HttpResponseRedirect 

# Create your views here.

import os, commands
from glob import glob
from subprocess import call
import requests

from .models import Codigo
from .forms import MyForm, CodigoForm


codigosI = ['''public class Main{
    public static void main(String args[]){
        System.out.println("Hola Mundito desde Java!!!!");
    }
}
''','print "Hola Mundito desde Python!!!!"','''#include <stdio.h>

int main( )
{
  printf("Hola Mundito desde c!!!!");
 return 0;
}

''','''#include <iostream>
int main() { 
  std::cout<< "Hola Mundito desde c++!!!!"; 
  return 0;
}'''
]



def index(request):

    output = ""
    username = None

    if request.user.is_authenticated():
        username = request.user.id
    codigos = Codigo.objects.filter(usuario=username)
    print codigos
    if request.method == 'POST':
        if 'ejecutar' in request.POST:
            print "ejecutar"
            # create a form instance and populate it with data from the request:
            form = CodigoForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                code = form.cleaned_data['codigo']
                print code
                lenguaje = form.cleaned_data['tipo']

                if lenguaje=="java":
                    # http://stackoverflow.com/questions/6159900/correct-way-to-write-line-to-file-in-python
                    f = open('Main.java', 'w')
                    f.write(code)  # python will convert \n to os.linesep
                    f.close()  # you can omit in most cases as the destructor will call it

                    # # http://stackoverflow.com/questions/24798256/difference-between-os-systemcmd-and-commands-getoutputcmd

                    b = commands.getoutput("javac Main.java")
                    c = commands.getoutput("java Main")

                if lenguaje=="python":
                    f = open('main.py', 'w')
                    f.write(code)  # python will convert \n to os.linesep
                    f.close()
                    b = commands.getoutput("python main.py")
                    c = "" 

                if lenguaje=="c":
                    f = open('main.c', 'w')
                    f.write(code)  # python will convert \n to os.linesep
                    f.close()  # you can omit in most cases as the destructor will call it

                    # # http://stackoverflow.com/questions/24798256/difference-between-os-systemcmd-and-commands-getoutputcmd

                    b = commands.getoutput("gcc -o mainc  main.c")
                    c = commands.getoutput("./mainc")

                if lenguaje=="cpp":
                    f = open('main.cpp', 'w')
                    f.write(code)  # python will convert \n to os.linesep
                    f.close()  # you can omit in most cases as the destructor will call it

                    # # http://stackoverflow.com/questions/24798256/difference-between-os-systemcmd-and-commands-getoutputcmd

                    b = commands.getoutput("g++ -o maincpp  main.cpp")
                    c = commands.getoutput("./maincpp")


                if b=="":
                    # Muestra Ejecucion de Codigo
                    output = c
                    output = output.replace("\n", "<br>")
                    output = output.replace(" ", "&nbsp;") # Boostrap
                else:
                    # Muestra Errores de Codigo
                    output = b
                    print output
                    output = output.replace("\n", "<br>")
                    output = output.replace(" ", "&nbsp;") # Boostrap
        else:
            form = CodigoForm(request.POST)
            if form.is_valid():
                codigo = form.cleaned_data['codigo']
                lenguaje = form.cleaned_data['tipo']
                nombre = form.cleaned_data['nombre']

                p = Codigo(nombre=nombre,codigo=codigo,tipo=lenguaje,usuario=request.user,publ_priv=True)
                p.save()
    else:
        form = CodigoForm()
        
    return render(request, 'index.html', {'form':form,'output':output,'codigos':codigos,'codigosI':codigosI})




def agregar(request):
    if request.POST == 'POST':
        formulario = CodigoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')

    else:
        formulario = CodigoForm()
    return render(request, 'editar.html', {'form':formulario})


def borrar(request, id):
    codigo = Codigo.objects.get(pk=id)
    codigo.delete()
    return HttpResponseRedirect("/")


def editar2(request, id):
    codigo = Codigo.objects.get(pk=id)
    if request.method == 'POST':
        formulario = CodigoForm(request.POST, instance=codigo)
        if formulario.is_valid():

            formulario.save()
    else:
        formulario = CodigoForm(instance=codigo)
    return render(request, 'editar.html', {'form':formulario})


def editar(request, id):

    output = ""
    username = None

    if request.user.is_authenticated():
        username = request.user.id
    codigo = Codigo.objects.get(pk=id)
    if request.method == 'POST':
        print "Llego 1"
        if 'ejecutar' in request.POST:
            print "ejecutar"
            # create a form instance and populate it with data from the request:
            form = CodigoForm(request.POST, instance=codigo)
            # check whether it's valid:
            if form.is_valid():
                print "hola"
                code = form.cleaned_data['codigo']
                print code
                lenguaje = form.cleaned_data['tipo']

                if lenguaje=="java":
                    # http://stackoverflow.com/questions/6159900/correct-way-to-write-line-to-file-in-python
                    f = open('Main.java', 'w')
                    f.write(code)  # python will convert \n to os.linesep
                    f.close()  # you can omit in most cases as the destructor will call it

                    # # http://stackoverflow.com/questions/24798256/difference-between-os-systemcmd-and-commands-getoutputcmd

                    b = commands.getoutput("javac Main.java")
                    c = commands.getoutput("java Main")

                if lenguaje=="python":
                    f = open('main.py', 'w')
                    f.write(code)  # python will convert \n to os.linesep
                    f.close()
                    b = commands.getoutput("python main.py")
                    c = "" 

                if lenguaje=="c":
                    f = open('main.c', 'w')
                    f.write(code)  # python will convert \n to os.linesep
                    f.close()  # you can omit in most cases as the destructor will call it

                    # # http://stackoverflow.com/questions/24798256/difference-between-os-systemcmd-and-commands-getoutputcmd

                    b = commands.getoutput("gcc -o mainc  main.c")
                    c = commands.getoutput("./mainc")

                if lenguaje=="cpp":
                    f = open('main.cpp', 'w')
                    f.write(code)  # python will convert \n to os.linesep
                    f.close()  # you can omit in most cases as the destructor will call it

                    # # http://stackoverflow.com/questions/24798256/difference-between-os-systemcmd-and-commands-getoutputcmd

                    b = commands.getoutput("g++ -o maincpp  main.cpp")
                    c = commands.getoutput("./maincpp")


                if b=="":
                    # Muestra Ejecucion de Codigo
                    output = c
                    output = output.replace("\n", "<br>")
                    output = output.replace(" ", "&nbsp;") # Boostrap
                else:
                    # Muestra Errores de Codigo
                    output = b
                    print output
                    output = output.replace("\n", "<br>")
                    output = output.replace(" ", "&nbsp;") # Boostrap
        else:
            codigo = Codigo.objects.get(pk=id)
            if request.method == 'POST':
                form = CodigoForm(request.POST, instance=codigo)
                if form.is_valid():
                    form.save()
    else:
        form = CodigoForm(instance=codigo)
        
    return render(request, 'index.html', {'form':form,'output':output,'codigosI':codigosI})
   




def codigos_usuario(request, usuario):
    codigos = Codigo.objects.filter(usuario=usuario)
    return render(request, 'codigos.html',{'codigos':codigos})


def codigo_usuario(request, usuario, id):
    codigos = Codigo.objects.filter(usuario=usuario)
    return render(request, 'codigos.html',{'codigos':codigos})

'''
[{"url":"http://localhost:8000/api/codigos/3/","nombre":"Hola Mundito","tipo":"java"},
{"url":"http://localhost:8000/api/codigos/4/","nombre":"Hola mundo en c","tipo":"cpp"}]
'''


def estadisticas(request):
    # http://stackoverflow.com/questions/4476373/simple-url-get-post-function-in-python
    url = 'http://localhost:8000/api/codigos/'
    # GET
    r = requests.get(url).json()
    lenguajesL = ['java', 'python', 'c', 'cpp']
    lenguajesC = {'java':0, 'python':0, 'c':0, 'cpp':0}

    for i in r:

        if i['tipo']=='java':
            lenguajesC['java']= lenguajesC['java']+1
        if i['tipo']=='python':
            lenguajesC['python']= lenguajesC['python']+1
        if i['tipo']=='c':
            lenguajesC['c']= lenguajesC['c']+1
        if i['tipo']=='cpp':
            lenguajesC['cpp']= lenguajesC['cpp']+1

    lenguajesCC = []      
    for i in lenguajesC:
        print i
        print lenguajesC[i]
        lenguajesCC.append([i,lenguajesC[i]])


    colores = ['#B02E12',"#A2B012","#55B012","#12B077","#1255B0"]
    cont = 0
    for l in lenguajesCC:
        l.append(colores[cont])
        cont=cont+1

    print lenguajesCC

    return render(request, 'estadisticas.html',{'lenguajesCC':lenguajesCC})


def index3(request):
    # http://stackoverflow.com/questions/37925521/how-to-embed-linux-terminal-in-django-based-webpage
    output = ""
    username = None
    if request.user.is_authenticated():
        username = request.user.id
    codigos = Codigo.objects.filter(usuario=username)
    print codigos
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MyForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            code = form.cleaned_data['codeeditor']

            print code
            f = open('Main.java', 'w')
            f.write(code)  # python will convert \n to os.linesep
            f.close()  # you can omit in most cases as the destructor will call it

            # http://stackoverflow.com/questions/24798256/difference-between-os-systemcmd-and-commands-getoutputcmd
            # http://stackoverflow.com/questions/3979888/in-python-scipting-how-do-i-capture-output-from-subprocess-call-to-a-file
            f = open('salida.txt','w')
            k = open('k.txt','w')
            wdir = ""

            # 1) list all .java files in directory
            for path in glob(os.path.join(wdir, "*.java")):
                # 2) compile the java file
                if call(['javac', path]) != 0: # error
                    continue
                # 3) if there is no error it then executes the file using its
                # class name which is same as file name
                classname = os.path.splitext(os.path.basename(path))[0]
                rc = call(['java', '-cp', wdir, classname], stdout=f,stdin=2)
                return render(request, 'index.html', {'form':form,'output':output,'codigos':codigos,'rc':rc})
                if rc != 0:
                    print('Error: classname: {} exit code: {}'.format(classname, rc))

            f.close()
            k.close()

            with open('salida.txt', 'r') as myfile:
                output=myfile.read()
    else:
        form = MyForm()
        
    return render(request, 'index.html', {'form':form,'output':output,'codigos':codigos})
