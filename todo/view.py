from django.shortcuts import render
from todoapp.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed= False).order_by('created_at')
    task_completed = Task.objects.filter(is_completed = True).order_by('created_at')
    context = {
        'tasks': tasks,
        'completed_tasks':  task_completed,  
        }
    return render(request, 'home-todo.html', context)