from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class TrainingCourse(models.Model):
    date = models.DateField(_('Date'), auto_now_add=False, auto_now=False)
    location = models.CharField(_('Location'),max_length=30, blank=False, null=False)
    topic = models.CharField(_('Topic'), max_length=150, blank=False, null=False)
    type = models.CharField(_('type'), max_length=150, blank=False, null=False)
    content = models.TextField(_('Content'),blank=True, null=True)

class AnnualTraningPlan(models.Model):
    training_course = models.ForeignKey(TrainingCourse)
    planned_date = models.DateField(_('Date'), auto_now_add=False, auto_now=False)
    actual_date = models.DateField(_('Date'), auto_now_add=False, auto_now=False, blank=True, null=True)