from django.shortcuts import render, redirect
from . task_form import TaskForm
from . models import Task

# Create your views here.
def index(request):
    data = Task.objects.all()
    return render(request, 'index.html', {'data':data})

def create_task(request):
    if request.method == "POST":
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('index')
            
    form1 = TaskForm()
    return render(request, 'create_task.html', {'form': form1})

