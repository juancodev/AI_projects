# metodo que me permite responder un status code de 404 y no detener el servidor
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, JsonResponse
from .models import Project
from .models import Task


# Create your views here.
def hello(request):
    return HttpResponse("Hello World")


def about(request):
    return HttpResponse("<h1>About</h1>")

def user(request, username):
    # Esta es la manera de obtener parámetros desde la URL
    print(username)
    # forma de concatenar un valor desde el método HttpResponse
    return HttpResponse("<h1>Hello %s</h1>" % username)

def projects(request):
    # De esta manera vamos a recibir un valor de tipo conjunto y no podemos responder eso del lado del cliente para eso necesitamos usar un formato JsonResponse.

    # Para obtener solamente los datos y no el modelo completo, lo hacemos enviando el método .values()
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def project_with_id(request, id):
    result = Project.objects.get(id=id)
    # Esto me sirve para hacer la consulta sin errores
    # primer argumento: el modelo y segundo argumento: la consulta
    result = get_object_or_404(Project, id=id)
    return HttpResponse("<h1>Projects: %s</h1>" % result.name)

def tasks(request: HttpRequest):
    print(request)
    return HttpResponse("<h1>Tasks</h1>")
