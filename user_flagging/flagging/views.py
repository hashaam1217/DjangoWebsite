from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Customer, Business, Flag 

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import *

# Create your views here.
def index(request):
    #return HttpResponseRedirect("list")
    return render(request, "flagging/index.html")
@api_view(["GET", "POST"])
def list(request):
    if request.method == "GET": 
        data = Customer.objects.all()
        
        serializer = CustomerSerializer(data, context={"request": request}, many=True)

        return Response(serializer.data)

    elif request.method == "POST":
        serializer = CustomerSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    #return render(request, "flagging/list.html", {
     #   "Customer": Customer.objects.all(),
      #  }) 

@api_view(["PUT", "DELETE"])
def customer(request, customer_id):
    try:
        customer = Customer.objects.get(pk=customer_id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = CustomerSerializer(customer, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    #return render(request, "flagging/list.html", {
     #   "Customer": Customer.objects.all(),
      #  }) 

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
