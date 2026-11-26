from django.shortcuts import render

def inicio (request):
    return render (request, "Ayala/inicio.html")
def Registro(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellidop = request.POST.get('apellidop')
        apellidom = request.POST.get('apellidom')
        edad = request.POST.get('edad')
        genero = request.POST.get('genero')
        intereses = request.POST.getlist('intereses')

        print('Tus datos registradosson: ')
        print('nombre: ',nombre)
        print('apellido paterno: ', apellidop)
        print('apellido materno: ', apellidom)
        print('edad:  ', edad )
        print('genero: ', genero)
        print('intereses: ', intereses)
    return render(request, "Ayala/formregistro.html")
def Taller (request):
    return render(request, "Ayala/formarte.html")


