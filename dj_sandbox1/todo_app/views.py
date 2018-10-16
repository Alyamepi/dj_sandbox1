from django.shortcuts import render
from .models import Task
from .forms import TaskForm
from django.shortcuts import redirect


def todolist(request):
    tasks = Task.objects.all()
    return render(
        request,
        'todo_app/todolist.html',
        {'tasks': tasks}
    )
def add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
            # de request wordt omgezet in een een form (de request heeft een veld "name" (zie html form in todolist.html))

        if form.is_valid():
            name = form.cleaned_data["name"]

            task = Task(name=name)
            task.save()

    return redirect('/todo/')

def delete(request, task_id):
    Task.objects.get(id=task_id).delete()
    return redirect('/todo/')

