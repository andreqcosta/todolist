from django.db import models

class ItemTodo(models.Model):
    item = models.CharField(max_length=100)
    done = models.BooleanField()