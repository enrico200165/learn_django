from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader


from scratch import do

def scratch(request):
    do()
    return(HttpResponse('Eseguito codice scratch, esaminare la console'))
