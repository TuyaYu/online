from django.shortcuts import render
from .serializer import GoodsSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Goods
# Create your views here.
class GoodsListView(APIView):
    """
    List all serializer, or create a new snippet.
    """
    def get(self, request, format=None):
        goods = Goods.objects.all()[:10]
        goods_serializer = GoodsSerializer(goods, many=True)
        return Response(goods_serializer.data)

