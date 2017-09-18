from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.utils import six, timezone

# Create your models here.
Crowdfunding_TYPE = (
	('health', 'Health'),
	('school', 'School'),
)

def image_upload_to(instance, filename):
    title = instance.title
    slug = slugify(title)
    basename, file_extension = filename.split(".")
    new_filename = "%s-%s.%s" %(slug[:100], instance.id, file_extension) #if it's new created object, the id is None
    #import time
    #new_filename = "%s-%s.%s" %(time.time(), slug, file_extension)    
    basename = basename
    username = instance.user.__unicode__()
    return "crowdfunding/%s/%s" %(username.lower(), new_filename)

class Crowdfunding(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	category = models.CharField(max_length=45, choices=Crowdfunding_TYPE)
	title = models.CharField(max_length=120)
	detail = models.TextField(blank=True, null=True)
	amount = models.DecimalField(max_digits=50, decimal_places=0, default=100)
	deadline = models.DateTimeField(_('deadline'), default=timezone.now)
	is_favorite = models.BooleanField(_('favorite status'), default=False,
        help_text=_('Designates whether this is favorite.'))
	image = models.ImageField(upload_to=image_upload_to)
	date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

	def __unicode__(self):
		return self.title

	# def get_absolute_url(self):
	# 	return reverse("crowdfunding", kwargs={})

	def get_absolute_url(self):
		return reverse("Crowdfunding_detail", kwargs={"pk": self.pk})

	def get_image_url(self):
		# img = self.productimage_set.first()
		img = self.image
		if img:
			return img.url
		return img #None		