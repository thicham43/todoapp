from django.utils import decorators
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Task
from .forms import TaskForm

from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from .serializers import TaskSerializer


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


#   **************************  api views   **************************


@api_view(['GET', 'POST', 'DELETE'])
def task_list(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        title = request.GET.get('title', None)
        if title is not None:
            tasks = tasks.filter(title__icontains=title)
        tasks_serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(tasks_serializer.data, safe=False)
    elif request.method == 'POST':
        task_data = JSONParser().parse(request)
        task_serializer = TaskSerializer(data=task_data)
        if task_serializer.is_valid():
            task_serializer.save()
            return JsonResponse(task_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Task.objects.all().delete()
        return JsonResponse({'message': '{} Tasks were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return JsonResponse({'message': 'The task does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        task_serializer = TaskSerializer(task)
        return JsonResponse(task_serializer.data)
    elif request.method == 'PUT':
        task_data = JSONParser().parse(request)
        task_serializer = TaskSerializer(task, data=task_data)
        if task_serializer.is_valid():
            task_serializer.save()
            return JsonResponse(task_serializer.data)
        return JsonResponse(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        task.delete()
        return JsonResponse({'message': 'Task was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
