from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns=[
    path('admin/',admin.site.urls),
]

urlpatterns=[
    path('',views.todo_list,name="todo_list"),
]

urlpatterns = [
    path("", views.todo_list,name='todo_list'),
    path('<int:pk>/',views.todo_detail,name='todo-detail')
]