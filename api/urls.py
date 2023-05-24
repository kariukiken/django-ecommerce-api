from django.urls import path
from .views import *

urlpatterns = [
    path('', StockList, name='stock_list'),
    path('add_stock', addstock, name='add_stock'),
    path('stock_history', stockhistory, name='stock_history'),
    path('category', category, name='category'),
    #path('stock_update/<int:pk>/', stock_update, name='stock_update'),
    path('api/items/search/', search_item_by_barcode, name='search_item_by_barcode'),
    path('items/<str:barcode>/subtract_quantity/', subtract_quantity, name='subtract_quantity'),
        #path('stock_update/<int:pk>/', StockUpdate, name='stock_update'),
]
