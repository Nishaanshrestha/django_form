from django.shortcuts import render, redirect
from . task_form import TaskForm
from . models import Task
from django.views import  View

class TaskView(View):
    def get(self,request):
        tasks=Task.objects.all()
        task_form=TaskForm()
        return render(request,'index.html',{'tasks':tasks,'tasks_form':task_form})
    
    def post(self,request):
        task_form=TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('home')
        task_form=TaskForm()
        return render(request,'index.html',{'form':task_form})
def update_task(request,id):
    task=Task.objects.get(id=id)
    if request.method=="POST":
        task_form=TaskForm(request.POST,instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('task')
    task_form=TaskForm(instance=task)
    return render(request,'index.html',{'form':task_form})

def delete_task(request,id):
    task=Task.objects.get(id=id)
    task.delete()
    return redirect('home')



# Create your views here.
# def index(request):
#     data = Task.objects.all()
#     return render(request, 'index.html', {'data':data})

# def create_task(request):
#     if request.method == "POST":
#         task_form = TaskForm(request.POST)
#         if task_form.is_valid():
#             task_form.save()
#             return redirect('index')
            
#     form1 = TaskForm()
#     return render(request, 'create_task.html', {'form': form1})

