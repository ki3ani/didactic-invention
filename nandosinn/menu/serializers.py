from .models import MenuItems
from rest_framework import serializers



class MenuItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItems
        fields = ('id', 'title', 'price', 'inventory')

        extra_kwargs = { 'inventory': {'min_value': 0},
                         'price': {'min_value': 2} }









