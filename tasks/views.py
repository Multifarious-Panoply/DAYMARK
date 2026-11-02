from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .forms import TaskForm
from .models import Task


def home(request):
    tasks = Task.objects.all()
    form = TaskForm()
    return render(request, "tasks/home.html", {
        "tasks": tasks,
        "form": form,
        "total_count": tasks.count(),
        "completed_count": tasks.filter(is_completed=True).count(),
        "pending_count": tasks.filter(is_completed=False).count(),
    })


def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect("home")


def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TaskForm(instance=task)
    return render(request, "tasks/edit.html", {"form": form, "task": task})


@require_POST
def toggle_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.is_completed = not task.is_completed
    task.save(update_fields=["is_completed"])
    return redirect("home")


@require_POST
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect("home")
