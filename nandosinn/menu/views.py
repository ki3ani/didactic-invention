
from .models import MenuItems
from .serializers import MenuItemsSerializer
from rest_framework import generics


# Create your views here.

class MenuItemsList(generics.ListCreateAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemsSerializer


class SingleMenuItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemsSerializer


    