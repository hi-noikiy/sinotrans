from django import forms
from django.forms.models import modelformset_factory
from django.utils.translation import ugettext_lazy as _

from .models import VehicleTransportationKPI

from inspection.models import month_choice

class VehicleTransportationKPIForm(forms.ModelForm):
    class Meta:
        model = VehicleTransportationKPI

        exclude = {
            'year',
            'month',
        }

vehicle_transportation_kpi_model_formset = modelformset_factory(VehicleTransportationKPI,
                                            form=VehicleTransportationKPIForm,
                                            extra=0)

class VehicleTransportationKPIFilterForm(forms.Form):
    year = forms.IntegerField(
        label=_('year'),
        initial=2017,
        required=False)

    month = forms.ChoiceField(
            label=_('month'),
            choices = month_choice,
            widget=forms.Select(),
            required=False
            ) 