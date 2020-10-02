from django.utils import decorators
from django.contrib.auth.decorators import login_required
from .models import Task
from django.views import generic


class TaskListView(generic.ListView):
    template_name = 'todo_app/index.html'
    context_object_name = 'all_tasks'

    # use: model or queryset or get_queryset
    def get_queryset(self):
        return Task.objects.all()

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['count_tasks'] = len(context_data['all_tasks'])
        return context_data


class TaskCreateView(generic.edit.CreateView):
    model = Task
    fields = ['title', 'comment', 'schedule_date']
    success_url = "/todo/"


class TaskUpdateView(generic.edit.UpdateView):
    model = Task
    fields = ['title', 'comment', 'schedule_date']
    success_url = "/todo/"


class TaskDeleteView(generic.edit.DeleteView):
    model = Task
    success_url = "/todo/"

    @decorators.method_decorator(login_required)
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

