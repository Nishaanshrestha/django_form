from django.urls import path
from . import views


urlpatterns = [
    path('', views.TaskView.as_view(), name='task'),
    path("delete_task/<int:id>", views.delete_task,name="delete_task"),
    path("update_task/<int:id>",views.update_task,name="update_task"),

]
