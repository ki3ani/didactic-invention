
from .models import MenuItems
from .serializers import MenuItemsSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


# Create your views here.
@api_view(['GET', 'POST'])
def MenuItemsList(request):
    items = MenuItems.objects.select_related('category').all()
    category_name = request.query_params.get('category', None)
    to_price = request.query_params.get('to_price', None)

    if category_name is not None:
        items = items.filter(category__name=category_name)
    
        serialized = MenuItemsSerializer(items, many=True)
        return Response(serialized.data)

    elif request.method == 'POST':
        serialized = MenuItemsSerializer(data=request.data)
    if serialized.is_valid(raise_exception=True):
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


