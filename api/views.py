from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from .models import *
from .serializers import *

# Create your views here.
@csrf_exempt
@api_view(['GET'])
def category(request):
    categories = Category.objects.all()
    serializer = categorySerializer(categories, many=True)
    return Response(serializer.data)

@csrf_exempt
@api_view(['GET'])
def StockList(request):
    stocks = Stock.objects.all()
    serializer = StockSerializer(stocks, many=True)
    return Response(serializer.data)

@csrf_exempt
@api_view(['GET'])
def stockhistory(request):
    stocks = StockHistory.objects.all()
    serializer = StockhistorySerializer(stocks, many=True)
    return Response(serializer.data)


@csrf_exempt
@api_view(['POST'])
def addstock(request):
    serializer = StockSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@csrf_exempt
@api_view(['GET'])
def search_item_by_barcode(request):
    barcode = request.GET.get('barcode', '')
    items = Stock.objects.filter(barcode=barcode)
    serializer = StockSerializer(items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


from django.http import JsonResponse

@csrf_exempt
@api_view(['POST'])
def subtract_quantity(request, barcode):
    item = get_object_or_404(Stock, barcode=barcode)
    quantity = request.data.get('quantity')
    if not quantity:
        return JsonResponse({'error': 'Quantity not provided'}, status=400)
    item.quantity -= quantity
    item.save()
    return JsonResponse({'success': 'Quantity subtracted from DB'})
