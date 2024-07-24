from django.urls import path

from task import views


urlpatterns = [
    path(
        "",
        views.TaskListView.as_view(),
        name="task-list"
    ),
    path(
        "create/",
        views.TaskCreateView.as_view(),
        name="task-create"
    ),
    path(
        "update/<int:pk>",
        views.TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "delete/<int:pk>",
        views.TaskDeleteView.as_view(),
        name="task-delete"),
    path(
        "<int:pk>/completion/",
        views.task_completion,
        name="task-completion"
    ),
    path(
        "tags/",
        views.TagsListView.as_view(),
        name="tag-list"),
    path(
        "tags/create/",
        views.TagsCreateView.as_view(),
        name="tag-create"
    ),
    path(
        "tags/update/<int:pk>",
        views.TagUpdateView.as_view(),
        name="tag-update"),
    path(
        "tags/delete/<int:pk>",
        views.TagDeleteView.as_view(),
        name="tag-delete"
    ),
]

app_name = "task"
