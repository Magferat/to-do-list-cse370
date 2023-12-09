from django import forms
from .models import MyTask
from datetime import datetime, time

class MyTaskForm(forms.ModelForm):
    class Meta:
        model = MyTask
        exclude = ['userID']  # Exclude the userID field from the form fields

        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'datetime-local'})
        }

    def __init__(self, *args, **kwargs):
        super(MyTaskForm, self).__init__(*args, **kwargs)

        default_time = time(hour=23, minute=59)  # 11:59 PM
        default_datetime = datetime.combine(datetime.today(), default_time)

        # Set the default value for the deadline field
        self.fields['deadline'].initial = default_datetime.strftime('%Y-%m-%dT%H:%M')

    def save(self, commit=True):
        task = super(MyTaskForm, self).save(commit=False)

        if 'userID' in self.initial:
            task.userID = self.initial['userID']  # Set the userID from the initial data if available

        if commit:
            task.save()

        return task