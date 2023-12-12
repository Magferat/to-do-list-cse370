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
from .models import MyTask, UserProfile, Note, Timer
from django.urls import reverse_lazy
import uuid
from .forms import MyTaskForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
# ====
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from .forms import TimerForm
from .utils import StudyTimer
import json
from .models import Note
from .forms import NoteForm



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


# ========



# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from .models import Timer
from .forms import TimerForm
import json


# def home(request):
#     return render(request, 'mytask_list.html')

def timer(request):
    form = TimerForm()
    return render(request, 'base/timer.html', {'form': form})
@require_POST
def set_timer(request):
    form = TimerForm(request.POST)
    if form.is_valid():
        form.save()
        timer_duration = form.cleaned_data['minutes'] * 60 + form.cleaned_data['seconds']
        data = {'timer_duration': timer_duration}
        return HttpResponse(json.dumps(data), content_type="application/json")
    return redirect('timer')


def my_notes(request):
    notes = Note.objects.all()
    return render(request, 'base/my_notes.html', {'notes': notes})

def create_note(request):
    form = NoteForm()

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.save()
            print(f"Note saved: {new_note.title} - {new_note.content}")
            return redirect('my_notes')
        else:
            print(f"Form errors: {form.errors}")

    return render(request, 'base/create_note.html', {'form': form})


def update_note(request, pk):
    note = Note.objects.get(id=pk)
    form = NoteForm(instance=note)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('my_notes')

    return render(request, 'base/update_note.html', {'form': form})

def delete_note(request, pk):
    note = Note.objects.get(id=pk)
    success_url = reverse_lazy('my_notes')
    if request.method == 'POST':
        note.delete()
        return redirect('my_notes')

    return render(request, 'base/delete_note.html', {'note': note})