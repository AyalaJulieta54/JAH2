from django.shortcuts import render

def inicio (request):
    return render (request, "Ayala/inicio.html")
def Registro(request):
    return render(request, "Ayala/formregistro.html")


