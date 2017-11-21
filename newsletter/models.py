from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=120, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self): #Python 3.3 is __str__
        return self.email


def image_upload_to_banner(instance, filename):
    title = instance.title
    slug = slugify(title)
    basename, file_extension = filename.split(".")
    new_filename = "%s.%s" %(slug, file_extension)
    basename = basename
    return "banner/%s" %(new_filename)

class Banner(models.Model):
    image = models.ImageField(verbose_name=_("image"), upload_to=image_upload_to_banner)
    title = models.CharField(verbose_name=_('title'), max_length=120, null=True, blank=True)
    text = models.CharField(verbose_name=_('text'), max_length=220, null=True, blank=True)
    active = models.BooleanField(verbose_name=_('active'), default=True)

    def __unicode__(self):
        return self.title      

    class Meta:
        verbose_name = _("banner")  
        verbose_name_plural = _("banner")  

def image_upload_to_article(instance, filename):
    title = instance.title
    slug = slugify(title)
    basename, file_extension = filename.split(".")
    new_filename = "%s.%s" %(slug, file_extension)
    basename = basename
    return "article/%s" %(new_filename)

class Article(models.Model):
    article_category = [
        ('news', _('news')),
        ('policy_and_information', _('policy and information')),
        ('organization_and_position_responsibility', _('organization and position responsibility')),
        ('road_risk_map', _('road risk map')),
    ]

    """docstring for Article"""
    category = models.CharField(verbose_name=_('category'), choices = article_category, max_length=150, blank=True, null=True, default="news")
    title = models.CharField(verbose_name=_('title'), max_length=150, blank=False, null=False)
    content = RichTextField(_('content'))
    publishtime = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name=_("publishtime"))
    abstract = models.TextField(_("abstract"), blank=False, null=False)
    image = models.ImageField(verbose_name=_("image"), upload_to=image_upload_to_article)

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.id })

    class Meta:
        verbose_name = _("artical")  
        verbose_name_plural = _("artical")  


