from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from task.forms import TaskForm, TagForm
from task.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "task/task_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


class TaskCreateView(generic.edit.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task:task-list")


def task_completion(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = not task.is_completed
    task.save()
    return redirect(reverse_lazy("task:task-list"))


class TagsListView(generic.ListView):
    model = Tag
    template_name = "task/tag_list.html"


class TagsCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("task:tag-list")
