from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views import View

from .forms import ReservationForm

# Create your views here.

# function-based view
def hello_world(Request: HttpRequest):
    return HttpResponse("Hello World")


# class based view
class HelloEthiopia(View):

    def get(self, request: HttpRequest):
        return HttpResponse("Hello Ethiopia")

def home(Request: HttpRequest):
    
    form = ReservationForm()

    if Request.method == "POST":
        form = ReservationForm(Request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Success")
    return render( Request, 'index.html', { 'form': form } )
