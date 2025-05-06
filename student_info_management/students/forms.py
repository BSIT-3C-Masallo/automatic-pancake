from django import forms
from .models import StudentInfo

class StudentInfoForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = ['name', 'address', 'email', 'gender', 'age', 'interest', 'course']  # ✅ Include 'course'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'address': forms.Textarea(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'rows': 3
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'gender': forms.Select(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-md bg-white focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'age': forms.NumberInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'interest': forms.Select(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-md bg-white focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'course': forms.Select(attrs={  # ✅ Add styling for course dropdown
                'class': 'w-full p-2 border border-gray-300 rounded-md bg-white focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
        }
