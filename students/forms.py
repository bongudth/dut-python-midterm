from django import forms
from .models import Department, Student

class StudentForms(forms.ModelForm):
    code = forms.CharField(label='MSSV', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'MSSV'
    }))

    name = forms.CharField(label='Tên', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Họ và tên'
    }))

    address = forms.CharField(initial='Việt Nam', label='Địa chỉ', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 10,
        'cols': 10,
    }))

    department = forms.ModelChoiceField(queryset=Department.objects.all(), label='Khoa', widget=forms.Select(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = Student
        fields = ['code', 'name', 'address', 'department']
