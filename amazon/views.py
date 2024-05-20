import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from amazon.models import Customer, Order, Return, Dispute
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializers import CustomerSerializer, OrderSerializer, ReturnSerializer, DisputeSerializer

DISPUTE_STATUS = ["RAISED", "ACTIVE", "INACTIVE", "CLOSED", "DUPLICATE"]


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_customer(request):
    """
    Save customer API
    """
    data = json.loads(request.body)
    serializer = CustomerSerializer(data=data)
    if serializer.is_valid():
        customer = serializer.save()
        return JsonResponse({"id": customer.customer_id})
    else:
        return JsonResponse({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_customers(request):
    """
    Get customers API
    """
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_order(request):
    """
    Save order API
    """
    data = json.loads(request.body)
    serializer = OrderSerializer(data=data)
    if serializer.is_valid():
        order = serializer.save()
        return JsonResponse({"id": order.order_id})
    else:
        return JsonResponse({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_orders(request):
    """
    Get orders API
    """
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_return(request):
    """
    Save return API
    """
    data = json.loads(request.body)
    serializer = ReturnSerializer(data=data)
    if serializer.is_valid():
        ret = serializer.save()
        return JsonResponse({"id": ret.return_id})
    else:
        return JsonResponse({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_returns(request):
    """
    Get returns API
    """
    returns = Return.objects.all()
    serializer = ReturnSerializer(returns, many=True)
    return Response(serializer.data)

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_dispute(request):
    """
    Save dispute API
    """
    data = json.loads(request.body)
    serializer = DisputeSerializer(data=data)
    if serializer.is_valid():
        dispute = serializer.save()
        return JsonResponse({"id": dispute.dispute_id})
    else:
        return JsonResponse({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_disputes(request):
    """
    Get disputes API
    """
    disputes = Dispute.objects.all()
    serializer = DisputeSerializer(disputes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def disputes_page(request):
    """
    Render dispute page
    """
    return render(request, "disputes.html")
