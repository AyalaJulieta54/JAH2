from django.shortcuts import render

def inicio (request):
    return render (request, "Ayala/inicio.html")
def Registro(request):
    return render(request, "Ayala/formregistro.html")
def Taller (request):
    return render(request, "Ayala/formarte.html")


