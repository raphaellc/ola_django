from django import forms
from .models import Pessoa

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'idade', 'email'] # alternativa para usar todos os campos -> '__all__'
        