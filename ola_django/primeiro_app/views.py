from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from .models import Pessoa
from .forms import PessoaForm, PessoaUpdateForm 
# Create your views here.
#criação da tela de cadastro de pessoa
class PessoaCreateView(CreateView):
    model = Pessoa
    form_class = PessoaForm
    template_name = 'cadastrar_pessoa.html'
    success_url = reverse_lazy('lista_pessoas')

class PessoaListView(ListView):
    model = Pessoa 
    template_name = 'lista_pessoas.html'

class PessoaUpdateView(UpdateView):
    model= Pessoa
    template_name = "editar_pessoa.html"
    form_class = PessoaUpdateForm
    success_url = reverse_lazy('lista_pessoas')