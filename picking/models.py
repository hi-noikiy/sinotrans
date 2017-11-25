from django.db import models

from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.db.models.signals import post_delete, post_save, pre_save
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
from django.http import Http404
from django.utils import timezone
from datetime import datetime, timedelta
from django.conf import settings

# Create your models here.


class Waybill(models.Model):
    number = models.CharField(_('waybill number'), max_length=30, blank=True)   
    forwarder = models.CharField(_('forwarder'), max_length=30, blank=True)    
    product_number = models.IntegerField(_('product number'), blank=True)    
    packing_number = models.IntegerField(_('packing number'), blank=True)   
    volume = models.DecimalField(_('volume'), max_digits=20, decimal_places=5, blank=True)    
    status = models.CharField(_('status'), max_length=30, blank=True) 
    created = models.DateField(_('created date'),auto_now_add=True, auto_now=False)
    completed = models.DateTimeField(_('completed time'),auto_now_add=False, auto_now=False)

    class Meta:
        ordering = ['number']
        verbose_name = _('waybill')
        verbose_name_plural =  _('waybill')

    def __unicode__(self):
        return self.number

class PickingBill(models.Model):
    waybill = models.ForeignKey(Waybill, verbose_name=_('waybill'))
    number = models.CharField(_('pickingbill number'), max_length=30, blank=True)    
    product_id = models.CharField(_('product id'), max_length=30, blank=True)    
    product_name = models.CharField(_('product name'), max_length=30, blank=True)    
    dispatch_bill_number = models.CharField(_('dispatch bill number'), max_length=30, blank=True)    
    waybill_number = models.CharField(_('waybill number'), max_length=30, blank=True)    
    product_total_number = models.IntegerField(_('product total number'),  blank=True)    
    packing_total_number = models.IntegerField(_('packing total number'),  blank=True)    
    volume = models.DecimalField(_('volume'), max_digits=20, decimal_places=5, blank=True)    
    status = models.CharField(_('status'), max_length=30, blank=True)   
    created = models.DateField(_('created date'),auto_now_add=True, auto_now=False)
    assigned = models.DateTimeField(_('assigned time'),auto_now_add=False, auto_now=False)

    class Meta:
        ordering = ['number']
        verbose_name = _('picking bill')
        verbose_name_plural =  _('picking bill')

    def __unicode__(self):
        return self.number    


