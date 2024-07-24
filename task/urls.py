from django.urls import path

from task.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    task_completion,
    TagsListView,
    TagsCreateView,
    TagUpdateView,
    TagDeleteView,
)

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('create/', TaskCreateView.as_view(), name='task-create'),
    path('update/<int:pk>', TaskUpdateView.as_view(), name='task-update'),
    path('delete/<int:pk>', TaskDeleteView.as_view(), name='task-delete'),
    path('<int:pk>/completion/', task_completion, name='task-completion'),
    path('tags/', TagsListView.as_view(), name='tag-list'),
    path('tags/create/', TagsCreateView.as_view(), name='tag-create'),
    path('tags/update/<int:pk>', TagUpdateView.as_view(), name='tag-update'),
    path('tags/delete/<int:pk>', TagDeleteView.as_view(), name='tag-delete'),
]

app_name = "task"
