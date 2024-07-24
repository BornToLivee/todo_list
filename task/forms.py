from django import forms

from task.models import Task, Tag


class TaskForm(forms.ModelForm):
    tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple(), required=True
    )

    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "deadline": forms.DateInput(attrs={"type": "datetime-local"}),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
