from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Customer, Business, Flag 
# Create your views here.
def index(request):
    return render(request, "flagging/index.html")

def list(request):
    return render(request, "flagging/list.html", {
        "Customer": Customer.objects.all(),
        }) 
