from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task, TaskCompletion, UserProfile

@login_required
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if not TaskCompletion.objects.filter(user=request.user, task=task).exists():
        TaskCompletion.objects.create(user=request.user, task=task)
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        profile.points += task.points
        profile.save()
    return redirect('task_list')

@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'tasks/profile.html', {'profile': user_profile})
      
