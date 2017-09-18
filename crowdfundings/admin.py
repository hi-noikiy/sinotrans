from django.contrib import admin

# Register your models here.
from .models import Crowdfunding

class CrowdfundingAdmin(admin.ModelAdmin):
	list_display = ['id', 'title','__unicode__', 'user', 'date_joined']

	class Meta:
		model = Crowdfunding

admin.site.register(Crowdfunding, CrowdfundingAdmin)
