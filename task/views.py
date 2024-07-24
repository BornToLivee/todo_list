from django.views import generic

from task.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "task_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


class TaskCreateView(generic.edit.CreateView):
    model = Task
