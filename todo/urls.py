from django.urls import path

from . import views

app_name = "todo"
urlpatterns = [
    path('', views.listtodo, name="listtodo"),
    path('<int:itemtodo_id>/done/', views.done, name="done"),
    path('<int:itemtodo_id>/delete/', views.delete, name="delete")
]