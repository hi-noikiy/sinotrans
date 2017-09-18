from django.contrib import admin

# Register your models here.
from .models import MPTTComment

class MPTTCommentAdmin(admin.ModelAdmin):
	list_display = ['id', 'parent',  '__unicode__', ]

	class Meta:
		model = MPTTComment

admin.site.register(MPTTComment, MPTTCommentAdmin)