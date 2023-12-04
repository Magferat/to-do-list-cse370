from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from .models import MyTask
from django.urls import reverse_lazy
import uuid

# Create your views here.

class All_Task(ListView):
    model = MyTask
    context_object_name = 'tasks'

class Task_Detail(DetailView):
      model = MyTask
      context_object_name = 'task'
      
      

class Add_New(CreateView):
    model = MyTask
    fields = '__all__'
    success_url = reverse_lazy('allTask')
    template_name = 'base/add_task.html'

    # def generate_unique_taskId(self):
    #     return uuid.uuid4().hex[:10]

    # def get_initial(self):
    #     initial = super().get_initial()
    #     initial['taskID'] = self.generate_unique_taskId()
    #     return initial

class Update_task(UpdateView):
     model = MyTask
     fields ='__all__'
     success_url = reverse_lazy('allTask')
     template_name = 'base/add_task.html'