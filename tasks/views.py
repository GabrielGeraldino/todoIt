from django.shortcuts import render, redirect, get_object_or_404
from tasks.models import Task

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {'Usuario': 'Dijkstra'})

def showTasks(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user)
        context = {'tasks': tasks}
        return render(request, "tasks/showTasks.html", context)

def newTask(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        category = request.POST.get('category')
        endDate = request.POST.get('endDate')
        user = request.user
        task = Task.objects.create(title=title, description=description, category=category, endDate=endDate, user=user)
        return redirect('list_task')
    return render(request, 'tasks/createTask.html')

def edit_task(request,task_id):
    task = Task.objects.get(id=task_id)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.category = request.POST.get('category')
        task.endDate = request.POST.get('endDate')
        task.save()

        return redirect('list_task')
    return render(request, 'tasks/editTask.html', {'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('list_task')