from django import forms
from tasks.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('titulo', 'prazo', 'descricao', 'finalizada')

    def clean_titulo(self):
        value = self.cleaned_data.get('titulo')
        if len(value) < 5:
            raise forms.ValidationError('O título deve ter no mínimo 5 caracteres.')
        return value