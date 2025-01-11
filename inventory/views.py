from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import F, Case, When, Value
from django.db import models
from django.urls import reverse_lazy
from .models import InventoryItem, Supplier, Order

class InventoryListView(ListView):
	model = InventoryItem
	template_name = 'inventory/list.html'
	context_object_name = 'items'
	paginate_by = 20

	def get_queryset(self):
		return InventoryItem.objects.order_by('name')

class InventoryDetailView(DetailView):
	model = InventoryItem
	template_name = 'inventory/detail.html'
	context_object_name = 'item'

class SupplierListView(ListView):
	model = Supplier
	template_name = 'inventory/suppliers.html'
	context_object_name = 'suppliers'

class SupplierDetailView(DetailView):
	model = Supplier
	template_name = 'inventory/supplier_detail.html'
	context_object_name = 'supplier'

class SupplierCreateView(CreateView):
	model = Supplier
	template_name = 'inventory/supplier_form.html'
	fields = ['name', 'contact_name', 'email', 'phone', 'address']
	success_url = reverse_lazy('supplier_list')

class SupplierUpdateView(UpdateView):
	model = Supplier
	template_name = 'inventory/supplier_form.html'
	fields = ['name', 'contact_name', 'email', 'phone', 'address']
	success_url = reverse_lazy('supplier_list')

class SupplierDeleteView(DeleteView):
	model = Supplier
	template_name = 'inventory/supplier_confirm_delete.html'
	success_url = reverse_lazy('supplier_list')

class InventoryItemCreateView(CreateView):
	model = InventoryItem
	template_name = 'inventory/item_form.html'
	fields = ['name', 'description', 'quantity', 'unit_cost', 'supplier', 'reorder_level']
	success_url = reverse_lazy('inventory_list')

class InventoryItemUpdateView(UpdateView):
	model = InventoryItem
	template_name = 'inventory/item_form.html'
	fields = ['name', 'description', 'quantity', 'unit_cost', 'supplier', 'reorder_level']
	success_url = reverse_lazy('inventory_list')

class InventoryItemDeleteView(DeleteView):
	model = InventoryItem
	template_name = 'inventory/item_confirm_delete.html'
	success_url = reverse_lazy('inventory_list')

def dashboard(request):
	low_stock_items = InventoryItem.objects.filter(
		quantity__lte=F('reorder_level')
	).order_by('name')
	
	recent_orders = Order.objects.order_by('-order_date')[:5]
	
	return render(request, 'inventory/dashboard.html', {
		'low_stock_items': low_stock_items,
		'recent_orders': recent_orders
	})

