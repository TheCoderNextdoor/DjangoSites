from django.shortcuts import render
from .serializer import StockSerializer
from .models import Stock
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


#list all stock or create a new one
#stocks/
class StockList(APIView):

    def get(self, request):
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)
        
        
    def post(self):
        pass
        