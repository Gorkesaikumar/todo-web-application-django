from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# Create your views here.
def addTask(request):
    taskVariable = request.POST['task']
    if taskVariable:
        Task.objects.create(task=taskVariable)
    return redirect('home')

def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        task.task = request.POST.get('task', task.task)
        task.save()
        return redirect('home')
    
    return render(request, 'edit_task.html', {'task': task})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')
