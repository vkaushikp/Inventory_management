from django.db import models
from django.core.validators import MinValueValidator

class Supplier(models.Model):
	name = models.CharField(max_length=255)
	contact_name = models.CharField(max_length=255)
	email = models.EmailField()
	phone = models.CharField(max_length=20)
	address = models.TextField()

	def __str__(self):
		return self.name

class InventoryItem(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	quantity = models.IntegerField(validators=[MinValueValidator(0)])
	unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
	supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
	reorder_level = models.IntegerField(default=10)
	last_updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.name} ({self.quantity} in stock)"

	@property 
	def total_value(self):
		return self.quantity * self.unit_cost


class Order(models.Model):
	ORDER_STATUS = [
		('P', 'Pending'),
		('C', 'Completed'),
		('X', 'Cancelled')
	]
	
	item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
	quantity = models.IntegerField(validators=[MinValueValidator(1)])
	order_date = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=1, choices=ORDER_STATUS, default='P')
	notes = models.TextField(blank=True)

	def __str__(self):
		return f"Order #{self.id} - {self.item.name}"

	def save(self, *args, **kwargs):
		if self.status == 'C' and self.pk:
			self.item.quantity += self.quantity
			self.item.save()
		super().save(*args, **kwargs)
