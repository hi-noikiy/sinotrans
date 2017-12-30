from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

def image_upload_to(instance, filename):
    name = instance.username
    title, file_extension = filename.split(".")
    new_filename = "%s-%s.%s" %(slugify(title), instance.id,  file_extension)
    return "profile/%s/%s" %(name, new_filename)

# Create your models here. 
class MyUser(AbstractUser):
    # image = models.ImageField(_('image'),upload_to=image_upload_to, blank=True, null=True)
    birthday = models.DateField(verbose_name=_('birthday'), blank=True, null=True)
                
    # class Meta(AbstractUser.Meta):
    #     swappable = 'AUTH_USER_MODEL'
    #     abstract = False