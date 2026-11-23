from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Job


class JobForm(forms.ModelForm):

    class Meta:
        model = Job

        fields = [
            'company_name',
            'job_title',
            'location',
            'job_type',
            'applied_date',
            'status',
            'description',
        ]

        widgets = {
            'company_name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'job_title': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'location': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'job_type': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'applied_date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
            'status': forms.Select(
                attrs={'class': 'form-select'}
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3
                }
            ),
        }


class RegisterForm(UserCreationForm):

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={'class': 'form-control'}
        )
    )

    class Meta:
        model = User

        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control'
            })