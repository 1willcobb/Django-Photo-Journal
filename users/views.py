from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def users(request):
    template = loader.get_template('./html/template.html')
    return HttpResponse(template.render())
