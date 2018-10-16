from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.todolist, name="ToDoList" ),
    path('add/', views.add, name = "AddToDo"),
    path('delete/<task_id>',views.delete, name = "DelToDo"),
]