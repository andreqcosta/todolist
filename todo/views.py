from django.shortcuts import render, redirect

from .forms import ItemTodoForm
from .models import ItemTodo

def listtodo(request):
    form = ItemTodoForm
    itemstodo = ItemTodo.objects.all()
    template = "todo/list.html"
    context = {'form': form, 'itemstodo': itemstodo}

    if request.POST:
        form = ItemTodoForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("todo:listtodo")

    return render(request, template, context)

def done(request, itemtodo_id):
    itemtodo = ItemTodo.objects.get(pk=itemtodo_id)
    itemtodo.done = not itemtodo.done
    print(itemtodo.done)
    itemtodo.save()
    return redirect("todo:listtodo")

def delete (request, itemtodo_id):
    itemtodo = ItemTodo.objects.get(pk=itemtodo_id)
    itemtodo.delete()
    return redirect("todo:listtodo")