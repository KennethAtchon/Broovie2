from django.shortcuts import render
from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer

# View to list all items
class ItemListView(generics.ListAPIView):
    queryset = Item.objects.all()  # Retrieve all items
    serializer_class = ItemSerializer
