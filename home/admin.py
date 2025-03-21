from django.contrib import admin

# Register your models here.
from .models import Departments,Doctors

admin.site.register(Departments)
admin.site.register(Doctors)