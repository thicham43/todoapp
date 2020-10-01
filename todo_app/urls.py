from django.urls import path
from . import views

app_name = "todo_app"
urlpatterns = [
                path('', views.index, name='index'),
                path('add', views.add_task, name='add_task'),
                path('edit/<int:task_id>', views.edit_task, name='edit_task'),
                path('remove/<int:task_id>', views.remove_task, name='remove_task'),
            ]