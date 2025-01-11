from django.contrib import admin
from .models import Supplier, InventoryItem, Order

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
	list_display = ('name', 'contact_name', 'email', 'phone')
	search_fields = ('name', 'contact_name')

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
	list_display = ('name', 'quantity', 'unit_cost', 'get_needs_reorder')
	list_filter = ('supplier',)
	search_fields = ('name',)
	readonly_fields = ('last_updated',)

	def get_needs_reorder(self, obj):
		return obj.quantity <= obj.reorder_level
	get_needs_reorder.short_description = 'Needs Reorder'
	get_needs_reorder.boolean = True

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ('id', 'item', 'quantity', 'status', 'order_date')
	list_filter = ('status',)
	search_fields = ('item__name',)
	readonly_fields = ('order_date',)
