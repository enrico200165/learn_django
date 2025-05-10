import os
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def members(request):
  print(os.getcwd())
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())