from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('ver_produto/', views.ver_produto, name='ver_produto'),
    path('inserir_produto/', views.inserir_produto, name='inserir_produto'),


]