from django.utils import decorators
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Task
from .forms import TaskForm


class TaskListView(generic.ListView):
    template_name = 'todo_app/list_task.html'
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
    form_class = TaskForm
    template_name = 'todo_app/add_task.html'
    success_url = "/todo/all"


class TaskUpdateView(generic.edit.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'todo_app/update_task.html'
    success_url = "/todo/all"


class TaskDeleteView(generic.edit.DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = "/todo/all"

    @decorators.method_decorator(login_required)
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class TaskSearchView(TaskListView):

    def get_queryset(self):
        return Task.objects.filter(title__icontains=self.request.GET[self.kwargs['q']])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['query'] = self.request.GET[self.kwargs['q']]
        return context_data

