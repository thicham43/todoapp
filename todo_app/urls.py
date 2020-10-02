from django.urls import path
from . import views

app_name = "todo_app"
urlpatterns = [
                path('', views.TaskListView.as_view(), name='index'),
                path('add/', views.TaskCreateView.as_view(), name='add_task'),
                path('<int:pk>', views.TaskUpdateView.as_view(), name='update_task'),
                path('delete/<int:pk>', views.TaskDeleteView.as_view(), name='delete_task'),
            ]