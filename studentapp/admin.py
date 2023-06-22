from django.contrib import admin
from .models import  Student,CLASS_CHOICES
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['admission_no', 'full_name','email','age','class_level','description','image','marklist']

admin.site.register(Student, StudentAdmin)

class ClassChoiceAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(CLASS_CHOICES, ClassChoiceAdmin)