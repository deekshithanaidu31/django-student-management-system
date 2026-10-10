
from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student

        fields = [
            'name',
            'email',
            'course',
            'age',
            'batch',
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter student name'
            }),

            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter email address'
            }),

            'course': forms.TextInput(attrs={
                'placeholder': 'Enter course name'
            }),

            'age': forms.NumberInput(attrs={
                'placeholder': 'Enter age',
                'min': 1
            }),

            'batch': forms.NumberInput(attrs={
                'placeholder': 'Enter batch year'
            }),
        }
