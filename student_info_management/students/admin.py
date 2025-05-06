from django.contrib import admin
from .models import StudentInfo

@admin.register(StudentInfo)
class StudentInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'gender', 'age', 'interest', 'course')
    search_fields = ('name', 'email', 'interest', 'course')
    list_filter = ('gender', 'interest', 'course')

# Register your models here.
