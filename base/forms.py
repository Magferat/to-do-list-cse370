from django import forms
from .models import MyTask, Timer, Note
from datetime import datetime, time
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column




class MyTaskForm(forms.ModelForm):
    class Meta:
        model = MyTask
        exclude = ['userID'] 

        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'datetime-local'})
        }

    def __init__(self, *args, **kwargs):
        super(MyTaskForm, self).__init__(*args, **kwargs)

        default_time = time(hour=23, minute=59)  
        default_datetime = datetime.combine(datetime.today(), default_time)

        self.fields['deadline'].initial = default_datetime.strftime('%Y-%m-%dT%H:%M')

    def save(self, commit=True):
        task = super(MyTaskForm, self).save(commit=False)

        if 'userID' in self.initial:
            task.userID = self.initial['userID'] 
        if commit:
            task.save()

        return task
    

# =============


class TimerForm(forms.ModelForm):
    class Meta:
        model = Timer
        fields = ['minutes', 'seconds']

        
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']

    def init(self, args, **kwargs):
        super().init(args, **kwargs)
