from django.shortcuts import get_object_or_404, render
from .models import Task, is_task_overdue
from django.views import generic


def index(request):
    if request.method == "POST":
        title = request.POST.get('title')
        comment = request.POST.get('comment')
        schedule_date = request.POST.get('schedule_date')
        task_overdue = is_task_overdue(schedule_date)
        if not request.POST.get('id'):
            Task.objects.create(title=title,
                                comment=comment,
                                schedule_date=schedule_date,
                                is_overdue=task_overdue[0],
                                days_overdue=task_overdue[1])
        else:
            task = Task.objects.get(id=request.POST.get('id'))
            task.title = title
            task.comment = comment
            task.schedule_date = schedule_date
            task.is_overdue = task_overdue[0]
            task.days_overdue = task_overdue[1]
            task.save()
    tasks = Task.objects.order_by("is_done", "schedule_date")
    return render(request, 'todo_app/index.html', {'tasks': tasks, 'count_tasks': len(tasks)})


def add_task(request):
    # open a popup that contains a form, close when submit and return to index
    return render(request, 'todo_app/add_task.html', {})


def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'todo_app/edit_task.html', {'task': task})


def remove_task(request, task_id):
    Task.objects.get(id=task_id).delete()
    return index(request)
