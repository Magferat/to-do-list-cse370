from django.contrib import admin
from .models import MyTask, UserProfile, Timer, Note

# Register your models here.

admin.site.register(MyTask)
admin.site.register(UserProfile)
admin.site.register(Timer)
admin.site.register(Note)
