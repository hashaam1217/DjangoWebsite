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

def customer(request, customer_id): 
    Current_Customer = Customer.objects.get(id=customer_id)
    flags = []
    for count in range(Current_Customer.flags.count()):
        current_flag = Current_Customer.flags.get(id=count+1)
        flags.append(current_flag)
        
    return render(request, "flagging/customer.html", {
        "customer_id":customer_id,
        "Customer": Current_Customer,
        "flags":flags
        })
