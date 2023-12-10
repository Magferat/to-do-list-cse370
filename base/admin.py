from django.contrib import admin
from .models import MyTask, UserProfile
# Register your models here.

admin.site.register(MyTask)
admin.site.register(UserProfile)
