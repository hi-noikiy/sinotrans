from django.contrib import admin

# Register your models here.
from .models import UserCheckout, UserAddress, Order

class UserCheckoutAdmin(admin.ModelAdmin):
	list_display = ['id', 'admin_user_id', '__unicode__', ]
	# inlines = [
	# 	UserInline,
	# ]
	class Meta:
		model = UserCheckout

class OrderAdmin(admin.ModelAdmin):
	list_display = ['id','status', 'user']

	class Meta:
		model = Order

admin.site.register(UserCheckout, UserCheckoutAdmin)

admin.site.register(UserAddress)

admin.site.register(Order, OrderAdmin)