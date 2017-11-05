from django import forms
from django.forms.models import modelformset_factory
from django.utils.translation import ugettext_lazy as _

from .models import VehicleTransportationKPI

from inspection.models import month_choice

class VehicleTransportationKPIForm(forms.ModelForm):

    # month = forms.ChoiceField(
    #         label=_('month'),
    #         widget=forms.TextInput(),
    #         required=False
    #         ) 

    class Meta:
        model = VehicleTransportationKPI

        exclude = {
            #'year',
            #'month',
        }

    def __init__(self, *args, **kwargs):
        super(VehicleTransportationKPIForm, self).__init__(*args, **kwargs)
        #instance = getattr(self, 'instance', None)
        #if instance and instance.pk:
        self.fields['year'].widget.attrs['readonly'] = True
        self.fields['month'].widget.attrs['readonly'] = True

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