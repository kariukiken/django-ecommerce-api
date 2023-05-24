from django.contrib import admin
from .models import *
from .forms import *

# Register your models here.

class StockCreateAdmin(admin.ModelAdmin):
   list_display =  ['category', 'subcategory', 'product_brand', 'item_name', 'barcode', 'quantity','unit_price', 'buying_price', 'last_updated']
   form = StockCreateForm
   #form = CategoryCreateForm
   list_filter = ['category']
   search_fields = ['category']

   def calculate_total_stock_profit(modeladmin, request, queryset):
    total_stock_profit = 0
    for stock in queryset:
        total_stock_profit += stock.total_profit()
    modeladmin.message_user(request, f'Expected Total Stock profit is: {total_stock_profit}')

    

   def  calculate_stock_value(modeladmin, request, queryset):
    total_value = 0
    for stock in queryset:
        total_value += stock.total
    modeladmin.message_user(request, f'Total stock value is: {total_value}')

   def calculate_unit_stock_profit(modeladmin, request, queryset):
    total_profit = 0
    for stock in queryset:
        total_profit += stock.profit()
    modeladmin.message_user(request, f'Expected Total profit is: {total_profit}')


   actions = [calculate_unit_stock_profit, calculate_stock_value, calculate_total_stock_profit]


class StockHistoryAdmin(admin.ModelAdmin):
   list_display =  ['category',  'item_name', 'quantity', 'buying_price', 'unit_price', 'receive_quantity', 'receive_by', 'issue_quantity', 'issue_by', 'issue_price',   'last_updated']
   form = StockHistoryForm
   list_filter = ['category', 'item_name']
   search_fields = ['category', 'item_name']


   def sales_profit(self, obj):
        if obj.issue_quantity and obj.issue_quantity != 0:
            return obj.total_profit() / obj.issue_quantity
        return 0
   sales_profit.short_description = "Profit per unit"
    

    #function to subtract buying_price values from issue_price columns
   def profits(self, obj):
        if obj.issue_price and obj.issue_quantity:
            return obj.issue_price - obj.buying_price
        return 0
   profits.short_description = 'Profits'
   profits.admin_order_field = 'profits'



    # function to add all the values in the total_profit column
   def calculate_total_profit(modeladmin, request, queryset):
        total_profit = 0
        for stock in queryset:
            total_profit += stock.total_profit()
        modeladmin.message_user(request, f'Total Profit : {total_profit}')

    # function to add all the values in the sales column
   def calculate_total_sales(modeladmin, request, queryset):
    total_sale = 0
    for stock in queryset:
        total_sale += stock.sales()
    modeladmin.message_user(request, f'Total sales: {total_sale}')
  

   actions = [calculate_total_sales, calculate_total_profit]




class CategoryCreateAdmin(admin.ModelAdmin):
	list_display = ['name']
	form = CategoryCreateForm
	list_filter = ['name']
	search_fields = ['name']

admin.site.register(Stock, StockCreateAdmin)
admin.site.register(StockHistory, StockHistoryAdmin)
admin.site.register(Category, CategoryCreateAdmin)