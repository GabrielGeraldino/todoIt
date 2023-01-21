from django.shortcuts import render
from tasks.models import Task

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {'Usuario': 'Dijkstra'})

def showTasks(request):
    tasks = Task.objects.order_by('title')
    context = {'Tasks': tasks}
    return render(request, "tasks/showTasks.html", context)

def newTask(request):
    return 

def edit_restaurant(request):
    return

def delete_restaurant(request):
    return