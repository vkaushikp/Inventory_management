"""
URL configuration for inventory_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from inventory import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='home'),
    path('inventory/', include([
        path('', views.InventoryListView.as_view(), name='inventory_list'),
        path('<int:pk>/', views.InventoryDetailView.as_view(), name='inventory_detail'),
        path('create/', views.InventoryItemCreateView.as_view(), name='inventory_create'),
        path('<int:pk>/update/', views.InventoryItemUpdateView.as_view(), name='inventory_update'),
        path('<int:pk>/delete/', views.InventoryItemDeleteView.as_view(), name='inventory_delete'),
    ])),
    path('suppliers/', include([
        path('', views.SupplierListView.as_view(), name='supplier_list'),
        path('<int:pk>/', views.SupplierDetailView.as_view(), name='supplier_detail'),
        path('create/', views.SupplierCreateView.as_view(), name='supplier_create'),
        path('<int:pk>/update/', views.SupplierUpdateView.as_view(), name='supplier_update'),
        path('<int:pk>/delete/', views.SupplierDeleteView.as_view(), name='supplier_delete'),
    ])),
]
