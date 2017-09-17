from django.contrib import admin
# Register your models here.
from .forms import SignUpForm
from .models import SignUp, Banner, Article

class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "timestamp", "updated"]
	form = SignUpForm
	# class Meta:
	# 	model = SignUp



class BannerAdmin(admin.ModelAdmin):
	list_display = [ "title", "text", "image","active"]
	class Meta:
		model = Banner

class ArticleAdmin(admin.ModelAdmin):
	list_display = ["title", "content",'image']
	class Meta:
		model = Article



admin.site.register(SignUp, SignUpAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Article, ArticleAdmin)
