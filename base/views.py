from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Product
from base.serializers import ProductSerializer
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView


routes = [
    '/api/v1/products/',
    '/api/v1/products/create',

    '/api/v1/products/upload/',

    '/api/v1/products/<id>/reviews/',

    '/api/v1/products/top/',
    '/api/v1/products/<id>/',

    '/api/v1/products/delete/<id>/',
    '/api/v1/products/<update>/<id>/',

]

@api_view(http_method_names=["GET"])
def GetRoutes(request):
    return Response(routes)


class GetProducts(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class GetProduct(APIView):
    def get(self , request , pk):
        query = Product.objects.get(pk = pk)
        serializer = ProductSerializer(query)
        return Response(serializer.data)
