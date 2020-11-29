from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Categoria
# Create your views here.


# class CategoriaIndex(ListView):
#     model = Categoria
#     template_name = 'parciais/_nav.html'
#     context_object_name = 'categorias'

#     def get_queryset(self):
#         qs = super().get_queryset()
#         return qs