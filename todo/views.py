from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import Task
from .forms import TaskForm

# Create your views here.
#a method to list tasks
def task_list(request):
    #all records in db
    tasks = Task.objects.all().order_by('-completed', '-id')  # Incomplete tasks first, newest on top
    return render(request, 'todo/task_list.html', {'tasks': tasks})



#a method to create the tasks
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task created successfully!')
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'todo/task_form.html', {'form': form})


def task_delete(request,pk):
    #getting task from model Task
    task = get_object_or_404(Task,pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request,'todo/task_confirm_delete.html',{'task':task})

def task_update(request,pk):
    task = get_object_or_404(Task,pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request,'todo/task_form.html',{'form':form})


#     task=Task.objects.get(id=id)
#     task.delete()
#     return render(request,'todo/task_list.html',{'tasks':tasks})
