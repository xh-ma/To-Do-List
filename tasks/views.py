from django.shortcuts import redirect, render
from .models import Task
from django.views.decorators.http import require_POST

def home(request):
    tasks = Task.objects.all()

    if request.method == 'POST':
        Task.objects.create(title=request.POST['title'])
        return redirect('home')
    tasks = Task.objects.all()
    return render(request, 'tasks/home.html', {'tasks': tasks})

@require_POST
def delete_task(request, task_id):
    Task.objects.get(id=task_id).delete()
    return redirect('/')

@require_POST
def toggle_complete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.complete = not task.complete
    task.save()
    return redirect('/')
