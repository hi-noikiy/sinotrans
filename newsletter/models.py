from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class SignUp(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length=120, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self): #Python 3.3 is __str__
		return self.email

'''
class UserWechat(models.Model):
	#user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True) #not required
	openid = models.CharField(max_length=120, blank=True, null=True)
	unionid = models.CharField(max_length=120, blank=True, null=True)
	city = models.CharField(max_length=120, blank=True, null=True)
	country = models.CharField(max_length=120, blank=True, null=True)	
	headimgurl = models.CharField(max_length=120, blank=True, null=True)
	language = models.CharField(max_length=120, blank=True, null=True)
	sex = models.CharField(max_length=120, blank=True, null=True)	
	privilege = models.CharField(max_length=120, blank=True, null=True)
	nickname = models.CharField(max_length=120, blank=True, null=True)

	def __unicode__(self): #def __str__(self):
		return self.nickname

	def admin_user_id(self):
		if self.user:
			return str(self.user.id)
		else:
			return "None" 

	def get_absolute_url(self):
		return reverse("personalcenter", kwargs={"id": self.id })
'''

def image_upload_to_banner(instance, filename):
	title = instance.title
	slug = slugify(title)
	basename, file_extension = filename.split(".")
	new_filename = "%s.%s" %(slug, file_extension)
	basename = basename
	return "banner/%s" %(new_filename)

class Banner(models.Model):
	image = models.ImageField(upload_to=image_upload_to_banner)
	title = models.CharField(max_length=120, null=True, blank=True)
	text = models.CharField(max_length=220, null=True, blank=True)
	active = models.BooleanField(default=True)

	def __unicode__(self):
		return self.title		

def image_upload_to_article(instance, filename):
	title = instance.title
	slug = slugify(title)
	basename, file_extension = filename.split(".")
	new_filename = "%s.%s" %(slug, file_extension)
	basename = basename
	return "article/%s" %(new_filename)

class Article(models.Model):
	"""docstring for Article"""
	title = models.CharField(verbose_name='title', max_length=150, blank=False, null=False)
	content = RichTextField('content')
	publishtime = models.DateTimeField(auto_now_add=True, auto_now=False)
	abstract = models.TextField(blank=False, null=False)
	image = models.ImageField(upload_to=image_upload_to_article)

	def get_absolute_url(self):
		return reverse("Article_detail", kwargs={"pk": self.id })		






