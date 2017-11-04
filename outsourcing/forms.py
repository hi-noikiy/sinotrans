from django import forms
from django.forms.models import modelformset_factory
from django.utils.translation import ugettext_lazy as _

from .models import VehicleTransportationKPI

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