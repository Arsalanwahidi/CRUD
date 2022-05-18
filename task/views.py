from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from task.forms import FormTask
from task.models import ModelTask
from django.views.decorators.cache import cache_control
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

@login_required(redirect_field_name='to', login_url='login')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):

    task = ModelTask.objects.all()
    
    return render(request, 'home.html', {'tasks': task})
    
@login_required(redirect_field_name='to', login_url='login/')
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


@login_required(redirect_field_name='to', login_url='login')
def delete(request, id):

    task = ModelTask.objects.get(pk=id)
    task.delete()
    return redirect('tasks:home')


@login_required(redirect_field_name='to', login_url='login')
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

def sign_up(request):
    
    
    # username = request.POST.get('username')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})