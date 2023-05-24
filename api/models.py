from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=50, blank=True, null=True)
	
	def __str__(self):
		return self.name

	
class Stock(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
	subcategory = models.CharField(max_length=50, blank=True, null=True)
	item_name = models.CharField(max_length=50, blank=True, null=True)
	quantity = models.IntegerField(default='0', blank=True, null=True)
	receive_quantity = models.IntegerField(default='0', blank=True, null=True)
	receive_by = models.CharField(max_length=50, blank=True, null=True)
	issue_quantity = models.IntegerField(default='0', blank=True, null=True)
	issue_price = models.IntegerField(default='0', blank=True, null=True)
	issue_by = models.CharField(max_length=50, blank=True, null=True)
	product_brand = models.CharField(max_length=50, blank=True, null=True)
	reorder_level = models.IntegerField(default='0', blank=True, null=True)
	last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	unit_price = models.IntegerField(default='0', blank=True, null=True)
	buying_price = models.IntegerField(default='0', blank=True, null=True)
	total_profit = models.IntegerField(default='0', blank=True, null=True)
	total = models.IntegerField(default='0', blank=True, null=True)
	stock_value = models.IntegerField(default='0', blank=True, null=True)
	sales = models.IntegerField(default='0', blank=True, null=True)
	loss = models.IntegerField(default='0', blank=True, null=True)
	barcode = models.IntegerField(default='0', blank=True, null=True)
	profit = models.IntegerField(default='0', blank=True, null=True)

	


	#multiplying quantity and unit_price column and saving in db
	def save(self, *args, **kwargs):
		self.total = self.quantity * self.unit_price
		super().save(*args, **kwargs)

	def profit(self):
		return self.unit_price - self.buying_price

	def total_profit(self):
		return self.quantity * self.profit()

	
	
		

class StockHistory(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
	item_name = models.CharField(max_length=50, blank=True, null=True)
	quantity = models.IntegerField(default='0', blank=True, null=True)
	receive_quantity = models.IntegerField(default='0', blank=True, null=True)
	receive_by = models.CharField(max_length=50, blank=True, null=True)
	issue_quantity = models.IntegerField(default='0', blank=True, null=True)
	issue_price = models.IntegerField(default='0', blank=True, null=True)
	unit_price = models.IntegerField(default='0', blank=True, null=True)
	issue_by = models.CharField(max_length=50, blank=True, null=True)
	issue_to = models.CharField(max_length=50, blank=True, null=True)
	phone_number = models.CharField(max_length=50, blank=True, null=True)
	created_by = models.CharField(max_length=50, blank=True, null=True)
	reorder_level = models.IntegerField(default='0', blank=True, null=True)
	last_updated = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)
	timestamp = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)
	sales = models.IntegerField(default='0', blank=True, null=True)
	loss = models.IntegerField(default='0', blank=True, null=True)
	total_profit = models.IntegerField(default='0', blank=True, null=True)
	buying_price = models.IntegerField(default='0', blank=True, null=True)
	profit = models.IntegerField(default='0', blank=True, null=True)



 
	def sales(self):
		return self.issue_quantity * self.issue_price

	def profit(self):
		return self.issue_price - self.buying_price

	def total_profit(self):
		return self.issue_quantity * self.profit()