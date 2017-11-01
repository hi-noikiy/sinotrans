from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.utils import timezone
from datetime import datetime, timedelta

from inspection.models import month_choice

# Create your models here.
class EquipmentType(models.Model):
    
    name = models.CharField(_('Name'), max_length=30, blank=False, null=False)

    class Meta:
        verbose_name = _('Equipment Type')
        verbose_name_plural = _('Equipment Type')

    def __unicode__(self):
        return "%s" % (self.name)

class Equipment(models.Model):

    name = models.CharField(_('Name'), max_length=30, blank=False, null=False) 
    type = models.ForeignKey(EquipmentType, verbose_name = _('Type'))

    class Meta:
        verbose_name = _('Equipment')
        verbose_name_plural = _('Equipment')

    def __unicode__(self):
        return "%s" % (self.name) 

class AbstractEquipmentInspection(models.Model):
    equipment_use_condition = (
        ('normal', _('Normal')),
        ('breakdown', _('Breakdown')),
    )

    equipment = models.ForeignKey(Equipment, verbose_name=_('Equipment'))
    use_condition = models.CharField(_('Use Condition'), choices=equipment_use_condition, max_length=30, blank=False,null=False,default='normal')
    inspector = models.CharField(_('Inspector'), max_length=30, blank=False,null=False)
    comments = models.TextField(_('Comments'), max_length=130, blank=True)   
    date_of_inspection = models.DateField(_('Date of Inspection'), auto_now_add=False, auto_now=False)
    updated = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = _('Equipment Inspection')
        verbose_name_plural = _('Equipment Inspection')
        abstract = True
        unique_together = (('equipment','inspector','date_of_inspection'),)

    def get_absolute_url(self):
        return reverse("equipmentinsepction_detail", kwargs={"pk": self.id})    

    def get_use_condition(self):
        return _('Normal') if self.use_condition == 'normal' else _('Breakdown')
        
class EquipmentInspectionManager(models.Manager):
    def get_query_set(self):
        return models.query.QuerySet(self.model, using=self._db)

    def get_this_day(self):
        start = timezone.now().date()
        end = start + timedelta(days=1)

        return self.get_query_set().filter(date_of_inspection__range=(start, end))


class EquipmentInspection(AbstractEquipmentInspection):
    objects = EquipmentInspectionManager()

    class Meta:
        abstract = False
        verbose_name = _('Equipment Inspection')
        verbose_name_plural = _('Equipment Inspection')
        
    def __unicode__(self):
        return "%s" % (self.equipment.name)    

class SprayPumpRoomInspectionManager(models.Manager):
    def get_query_set(self):
        return models.query.QuerySet(self.model, using=self._db)

    def queryset_ordered(self):
        # queryset = []
        # for month in month_choice:
        #     queryset.append(self.get_query_set().filter(month=month[0]))
        # return queryset

        return self.get_query_set().all()

class SprayPumpRoomInspection(models.Model):
    month = models.CharField(_('Month'), choices=month_choice, max_length=30, blank=False,null=False)
    voltage_and_power_normal = models.BooleanField(_('voltage and power normal'), blank=True, default=False)
    indicator_and_instrument_normal = models.BooleanField(_('indicator and instrument normal'), blank=True, default=False)
    inspector = models.CharField(_('Inspector'), max_length=30, blank=False,null=False)
    date_of_inspection = models.DateField(_('Date of Inspection'), auto_now_add=False, auto_now=False,default='1970-01-01')

    objects = SprayPumpRoomInspectionManager()
    def __unicode__(self):
        return _("Spray Pump Room Inspection") + " %s" % (self.month)

    class Meta:
        ordering = ('month',)
        verbose_name = _("Spray Pump Room Inspection")
        verbose_name_plural = _("Spray Pump Room Inspection")
        #unique_together = (('month','yera',),)        