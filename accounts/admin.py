from django.contrib import admin
from .models import Student, Volunteer, Administrator
# Register your models here.

admin.site.register(Student)
admin.site.register(Volunteer)
admin.site.register(Administrator)
