from django.contrib import admin

# Register your models here.
from .models import Cart, CartItem
from orders.models import Order

class OrderInline(admin.TabularInline):
	model = Order
	extra = 0

class CartItemInline(admin.TabularInline):
	model = CartItem
	extra = 0

class CartAdmin(admin.ModelAdmin):
	list_display = ['id','user', 'updated']
	inlines = [
		CartItemInline,
		OrderInline
	]
	class Meta:
		model = Cart


admin.site.register(Cart, CartAdmin)