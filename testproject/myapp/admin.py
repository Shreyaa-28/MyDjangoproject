from django.contrib import admin

# Register your models here.
from . models import Student

admin.site.register(Student)

from . models import Subject

admin.site.register(Subject)