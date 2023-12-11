from django.urls import path
from .views import All_Task, Task_Detail, Add_New, Update_task, DeleteView, CustomLoginView, RegisterPage, HomePageView
from django.contrib.auth.views import LogoutView
from .views import timer, set_timer, store_study_session
from .views import my_notes, create_note, update_note, delete_note


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('home/', HomePageView.as_view(), name='home'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', All_Task.as_view(), name='allTask'),
    # path('', All_Task.as_view(), name='allTask'),
    path('task/<int:pk>/', Task_Detail.as_view(), name='task'),
    path('add-task/', Add_New.as_view(), name='add_task'),
    
    path('task-edit/<int:task_id>/', Update_task.as_view(), name='task-edit'),

    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),

    # path('home/', home, name='home'),
    path('timer/', timer, name='timer'),
    path('set_timer/', set_timer, name='set_timer'),
    path('store_study_session/', store_study_session, name='store_study_session'),
    
    path('my_notes/', my_notes, name='my_notes'),
    path('create_note/', create_note, name='create_note'),
    path('update_note/<str:pk>/', update_note, name='update_note'),
    path('delete_note/<str:pk>/', delete_note, name='delete_note'),
    # path('mytask_list/', views.mytask_list, name='mytask_list'),

]