from django.urls import path
from django.http import HttpResponse
from .views import PessoaCreateView, PessoaListView, PessoaUpdateView

def oiDjango(resquest):
    return HttpResponse('Olá primeiroAPP')

urlpatterns = [
    path('olaApp/', oiDjango),
    path('cadastrar_pessoa/', PessoaCreateView.as_view(), name='cadastrar_pessoa'),
    path('listar_pessoa/', PessoaListView.as_view(), name='lista_pessoas'),
    path('pessoas/<int:pk>/editar/', PessoaUpdateView.as_view(), name='editar_pessoa'),
]