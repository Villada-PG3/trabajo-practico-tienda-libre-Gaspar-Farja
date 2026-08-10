from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView


class inicio(TemplateView):
    template_name = 'inicio.html'


class acerca_de_mi(TemplateView):
    template_name = 'acerca_de_mi.html'