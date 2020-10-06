from django.urls import path
from . import views

app_name = "todo_app"
urlpatterns = [
                path('all/', views.TaskListView.as_view(), name='index'),
                path('add/', views.TaskCreateView.as_view(), name='add_task'),
                path('<int:pk>', views.TaskUpdateView.as_view(), name='update_task'),
                path('<int:pk>/delete/', views.TaskDeleteView.as_view(), name='delete_task'),
                path('search/<q>', views.TaskSearchView.as_view(), name='search_task'),
                ]