from django import forms
from .models import *

class StockCreateForm(forms.ModelForm):
        class Meta:
         model = Stock
         fields = ['category', 'subcategory', 'product_brand', 'item_name', 'barcode', 'quantity','unit_price', 'buying_price']

class CategoryCreateForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ['name']

class StockHistoryForm(forms.ModelForm):
	class Meta:
		model = StockHistory
		fields =  ['category',  'item_name', 'quantity', 'buying_price', 'unit_price', 'receive_quantity', 'receive_by', 'issue_quantity', 'issue_by', 'issue_price',   'last_updated']

