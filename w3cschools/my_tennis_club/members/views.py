from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.

def members(request):
    # return HttpResponse("Hellow World!")
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())