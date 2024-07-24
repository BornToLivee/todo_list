from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    tag = models.ManyToManyField("Tag", related_name="tasks")

    class Meta:
        ordering = ["is_completed", "-created_at"]

    def __str__(self):
        return self.content
