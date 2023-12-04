from django.urls import path
from .views import All_Task, Task_Detail, Add_New, Update_task

urlpatterns = [
    path('', All_Task.as_view(), name='allTask'),
    path('task/<int:pk>/', Task_Detail.as_view(), name='task'),
    path('add-task/', Add_New.as_view(), name='add_task'),
    path('task-edit/<int:pk>/', Update_task.as_view(), name='task-edit')

]