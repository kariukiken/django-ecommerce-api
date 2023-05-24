from rest_framework import serializers
from .models import *

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

class StockhistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = StockHistory
        fields = '__all__'

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

