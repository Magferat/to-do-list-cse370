from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, FormView
from django.views.generic.edit import UpdateView
from .models import MyTask
from django.urls import reverse_lazy
import uuid
from .forms import MyTaskForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.


class CustomLoginView(LoginView):
     template_name = 'base/login.html'
     fields = '__all__'
     redirect_authenticated_user = True

     def get_success_url(self):
          return reverse_lazy('allTask')


class RegisterPage(FormView):
     template_name = 'base/register.html'
     form_class = UserCreationForm
     redirect_authenticated_user = True
     success_url = reverse_lazy('allTask')

     def form_valid(self, form):
          user = form.save()
          if user is not None:
               login(self.request, user)
          return super(RegisterPage,self).form_valid(form)

# class All_Task(LoginRequiredMixin, ListView):
#     model = MyTask
#     ordering = ['deadline'] 
#     context_object_name = 'tasks'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['tasks'] = context['tasks'].filter(userID=self.request.user)
#         context['count'] = context['tasks'].filter(status=False).count()  
#         return context
class All_Task(LoginRequiredMixin, ListView):
    model = MyTask
    ordering = ['deadline'] 
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        # Filter unfinished 
        unfinished_tasks = MyTask.objects.filter(userID=user, status=False)
        
        # Filter finished 
        finished_tasks = MyTask.objects.filter(userID=user, status=True)
        
        context['unfinished_tasks'] = unfinished_tasks
        context['finished_tasks'] = finished_tasks
        context['count_unfinished'] = unfinished_tasks.count()  
        return context


class Task_Detail(LoginRequiredMixin,DetailView):
      model = MyTask
      context_object_name = 'task'

      

class Add_New(LoginRequiredMixin,CreateView):
    model = MyTask
    form_class = MyTaskForm
    success_url = reverse_lazy('allTask')
    template_name = 'base/add_task.html'

    def form_valid(self, form):
         form.instance.userID = self.request.user
         return super(Add_New,self).form_valid(form)


class Update_task(LoginRequiredMixin,UpdateView):
     model = MyTask
     form_class = MyTaskForm
    #  fields = ['title', 'discription', 'deadline', 'status' ]
    #  fields ='__all__'
     success_url = reverse_lazy('allTask')
     template_name = 'base/add_task.html'

class DeleteView(LoginRequiredMixin, DeleteView):
     model= MyTask
     context_object_name = 'task'
     success_url = reverse_lazy('allTask')
