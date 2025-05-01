from django import forms
from .models import Project
from django.utils import timezone
from django.core.exceptions import ValidationError

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'area', 'objectives', 
                 'keywords', 'project_type', 'requirements',
                 'start_date', 'end_date', 'is_open', 'role_required']
        widgets = {
            'start_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'min': timezone.now().strftime('%Y-%m-%d')
            }),
            'end_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'rows': 3,
                'class': 'form-control'
            }),
            'objectives': forms.Textarea(attrs={
                'rows': 3,
                'class': 'form-control'
            }),
            'requirements': forms.Textarea(attrs={
                'rows': 2,
                'class': 'form-control'
            })
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date and end_date < start_date:
            raise ValidationError("La fecha de término no puede ser anterior a la fecha de inicio")
        
        return cleaned_data