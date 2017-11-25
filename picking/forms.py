from django import forms
from django.forms.models import modelformset_factory
from django.utils.translation import ugettext_lazy as _

from .models import PickingBill



class PickingBillScanForm(forms.Form):
    number = forms.CharField(
        label=_('pickingbill number'),
        widget=forms.Textarea(),        
        required=True)

    picking_staff = forms.CharField(
        label=_('picking staff'),
        required=True
        ) 

class WaybillScanForm(forms.Form):
    number = forms.CharField(
        label=_('waybill number'),
        widget=forms.Textarea(),
        required=True)

    label_staff = forms.CharField(
        label=_('label staff'),
        required=True
        )  

    distribution_staff = forms.CharField(
        label=_('distribution staff'),
        required=True
        )