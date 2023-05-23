from django.db import models

# Create your models here.
class TodoList(models.Model):
    todos = models.CharField(max_length=30)
    description = models.TextField()
    important = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.todos} [{self.id}]'