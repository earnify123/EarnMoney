from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('complete_task/<int:task_id>/', views.complete_task, name='complete_task'),
    path('profile/', views.profile, name='profile'),
]

