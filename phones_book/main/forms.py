from .models import Department, Staff
from django.forms import ModelForm, TextInput, Textarea, NumberInput, DateInput, Select

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ["title", "description", "staff_count"]

        widgets = {
            "title": TextInput(attrs={
                'class': 'form_field',
                'placeholder': 'Название отдела',
            }),
            "description": Textarea(attrs={
                'class': 'form_field',
                'placeholder': 'Описание отдела',
            }),
            "staff_count": NumberInput(attrs={
                'class': 'form_field',
                'placeholder': 'Число сотрудников',
            }),
        }

class StaffForm(ModelForm):
    class Meta:
        model = Staff
        fields = ["first_name", "last_name", "phone", "department", "post", "experience", "date"]

        widgets = {
            "first_name": TextInput(attrs={
                'class': 'form_field',
                'placeholder': 'Имя',
            }),
            "last_name": TextInput(attrs={
                'class': 'form_field',
                'placeholder': 'Фамилия',
            }),
            "phone": NumberInput(attrs={
                'class': 'form_field',
                'placeholder': 'Телефон',
            }),
            "department": Select(attrs={
                'class': 'form_field',
            }),
            "post": TextInput(attrs={
                'class': 'form_field',
                'placeholder': 'Должность',
            }),
            "experience": NumberInput(attrs={
                'class': 'form_field',
                'placeholder': 'Стаж работы',
            }),
            "date": DateInput(attrs={
                'class': 'form_field',
                'placeholder': 'Дата приема на работу',
            }),
        }