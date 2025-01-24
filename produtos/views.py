from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def ver_produto(request):
    nome = ani
    return render(request, 'ver_produto.html',{'nome':nome})


def inserir_produto(request):
    return  render(request, 'inserir_produto.html')