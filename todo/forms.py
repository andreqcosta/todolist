from django import forms
from .models import ItemTodo

class ItemTodoForm(forms.ModelForm):
    class Meta:
        model = ItemTodo
        fields = '__all__'