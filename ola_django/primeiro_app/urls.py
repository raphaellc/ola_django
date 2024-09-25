from django.urls import path
from django.http import HttpResponse
from .views import PessoaCreateView, PessoaListView

def oiDjango(resquest):
    return HttpResponse('Olá primeiroAPP')

urlpatterns = [
    path('olaApp/', oiDjango),
    path('cadastrar_pessoa/', PessoaCreateView.as_view(), name='cadastrar_pessoa'),
    path('listar_pessoa/', PessoaListView.as_view(), name='lista_pessoas'),
    #path('cadastrar_pessoa/listar_pessoa/', PessoaListView.as_view(), name='lista_pessoas'),
]