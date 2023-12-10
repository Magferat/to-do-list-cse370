from django.urls import path
from .views import All_Task, Task_Detail, Add_New, Update_task, DeleteView, CustomLoginView, RegisterPage, HomePageView
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
     path('home/', HomePageView.as_view(), name='home'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('tasks/', All_Task.as_view(), name='allTask'),

    # path('', All_Task.as_view(), name='allTask'),
    path('task/<int:pk>/', Task_Detail.as_view(), name='task'),
    path('add-task/', Add_New.as_view(), name='add_task'),
    path('task-edit/<int:pk>/', Update_task.as_view(), name='task-edit'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete')


]