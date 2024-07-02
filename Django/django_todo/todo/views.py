from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import TodoItem
from .forms import TodoForm


def index(request):
    todo_items = TodoItem.objects.all()
    return render(request, 'todo/index.html', {'todo_items': todo_items})


def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm()
    return render(request, 'todo/add_todo.html', {'form': form})


def update_todo(request, todo_id):
    todo_item = get_object_or_404(TodoItem, id=todo_id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo_item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm(instance=todo_item)
    return render(request, 'todo/update_todo.html', {'form': form})


def delete_todo(request, todo_id):
    todo_item = get_object_or_404(TodoItem, id=todo_id)
    todo_item.delete()
    return redirect('index')
