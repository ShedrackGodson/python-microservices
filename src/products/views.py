import random

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from .serializers import ProductSerializer
from django.shortcuts import render
from .models import Product, User


class ProductViewSet(ViewSet):
    # Define CRUD methods
    def list(self, request):  # /api/products/
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(data=serializer.data, status=200)

    def create(self, request):  # /api/product/create/
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):  # /api/product/<str: id>/get/
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):  # /api/product/<str: id>/update/
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):  # /api/product/<str: id>/delete/
        Product.objects.get(id=pk).delete()
        return Response(status=status.HTTP_200_OK)


class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            "id": user.id
        })
