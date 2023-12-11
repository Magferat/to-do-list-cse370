from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, FormView
from django.views.generic.edit import UpdateView
from django.views.generic import TemplateView
from .models import MyTask, UserProfile
from django.urls import reverse_lazy
import uuid
from .forms import MyTaskForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.


class CustomLoginView(LoginView):
     template_name = 'base/login.html'
     fields = '__all__'
     redirect_authenticated_user = True

     def get_success_url(self):
          return reverse_lazy('home')


class RegisterPage(FormView):
     template_name = 'base/register.html'
     form_class = UserCreationForm
     redirect_authenticated_user = True
     success_url = reverse_lazy('allTask')

     def form_valid(self, form):
          user = form.save()

          UserProfile.objects.create(user= user)
          if user is not None:
               login(self.request, user)
          return super(RegisterPage,self).form_valid(form)

class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'base/home.html'

class All_Task(LoginRequiredMixin, ListView):
    model = MyTask
    ordering = ['deadline'] 
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        unfinished_tasks = MyTask.objects.filter(userID=user, status=False)
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


class Update_task(LoginRequiredMixin, UpdateView):
    model = MyTask
    form_class = MyTaskForm
    success_url = reverse_lazy('allTask')
    template_name = 'base/edit_task.html'

    def get_object(self, queryset=None):
        task_id = self.kwargs.get('task_id')
        return get_object_or_404(MyTask, pk=task_id)

    def form_valid(self, form):
        form.instance.userID = self.request.user
        return super(Update_task, self).form_valid(form)

class DeleteView(LoginRequiredMixin, DeleteView):
     model= MyTask
     context_object_name = 'task'
     success_url = reverse_lazy('allTask')
