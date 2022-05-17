from django.shortcuts import redirect, render, get_object_or_404
from sympy import Id
from task.forms import FormTask
from task.models import ModelTask

# Create your views here.


def home(request):

    task = ModelTask.objects.all()
    
    return render(request, 'home.html', {'tasks': task})
    

def create(request):

    form = FormTask()
    if request.method == 'POST':

        title = request.POST.get('title_task')
        description = request.POST.get('description_task')
        start = request.POST.get('start_date')
        end = request.POST.get('end_date')

        ModelTask.objects.create(title_task=title, description_task=description, start_date=start, end_date=end)
        
        return redirect('tasks:home')
    else:
        return render(request, 'create.html', {'form': form})


def delete(request, id):

    task = ModelTask.objects.get(pk=id)
    task.delete()
    return redirect('tasks:home')

def update(request, id):
    
    task = get_object_or_404(ModelTask, pk=id)
    form = FormTask(request.POST, instance=task)

    if request.method == 'POST':
        task.title_task = request.POST.get('title_task')
        task.description_task = request.POST.get('description_task')
        task.start_date = request.POST.get('start_date')
        task.end_date = request.POST.get('end_date')
        task.save()

        return redirect('tasks:home')

    else:
        return render(request, 'update.html', {'form': form, 'task': task})
