from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from customers.models import Customer
from customers.serializers import CustomerSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.
def CustomerApiView(request):
    return HttpResponse("Hello, API.")

def CustomerHomeApiView(request):
    customers = Customer.objects.all()
    customers_list = list(customers.values())
    return JsonResponse(customers_list,safe=False)

@api_view(['GET','POST'])
def CustomerListApiView(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
           return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def CustomerDetailApiView(request,id):
    try:
        customer = Customer.objects.get(id=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = CustomerSerializer(customer)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = CustomerSerializer(customer,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





