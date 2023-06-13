from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo

from django.views.decorators.http import require_http_methods

# Create your views here.

def index(request):
    todos = Todo.objects.all().order_by('-date_create')
    context = {
        'title': 'Новое задания',
        'todolist': todos
    }

    return render(request, 'todoapp/index.html', context)

@require_http_methods(['POST'])
def add(request):
    title = request.POST['title']
    todo = Todo(title=title)
    todo.save()
    return redirect('index')

def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('index')

def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')
