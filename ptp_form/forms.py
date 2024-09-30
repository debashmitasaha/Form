from django import forms
from .models import PreTaskForm

class PreTaskFormModelForm(forms.ModelForm):
    class Meta:
        model = PreTaskForm
        fields = '__all__'
