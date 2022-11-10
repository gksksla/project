from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.todo_list, name="todo_list"),
    path('<int:pk>/', views.todo_detail, name='todo-detail')
]
