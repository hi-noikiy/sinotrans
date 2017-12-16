from django import forms
from django.forms.models import modelformset_factory
from django.utils.translation import ugettext_lazy as _

from .models import VehicleTransportationKPI, VehicleInspection, ForkliftRepair, ForkliftAnnualInspectionImage
from django.contrib.auth import get_user_model
from inspection.models import month_choice
from inspection.forms import ImageFileInput

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
        min_value=2017,
        required=False)

    month = forms.ChoiceField(
            label=_('month'),
            choices = month_choice,
            widget=forms.Select(),
            required=False
            ) 

class VehicleInspectionForm(forms.ModelForm):
    owner = forms.ChoiceField(
            label=_('Owner'),
            choices = set((ins, ins) for ins in get_user_model().objects.all()),
            # widget=forms.RadioSelect(),
            required=True
            )           

    def __init__(self, *args, **kwargs):
        super(VehicleInspectionForm, self).__init__(*args, **kwargs)
        self.fields['completed_time'].widget.attrs['disabled'] = True
        self.fields['inspector'].widget.attrs['readonly'] = True

    class Meta:
        model = VehicleInspection

        exclude = {
            "inspector",
        }        

    def clean_rectification_qualified(self):
        rectification_qualified = self.data['rectification_qualified']

        if "yes" == rectification_qualified and not self.data["disqualification_comments"]:
            raise forms.ValidationError(_('comments requierd to change it to yes!'))
            return rectification_qualified
        elif "no" == rectification_qualified:
            fields = [
                "hardware_inspection_disqualification",        
                "no_driver_code_of_conduct",
                "overload_or_LSR_violation",
                "safety_policy_violation",
                "no_journey_plan_or_log",
                "vehichle_not_register",
                "no_vehicle_inspection_record",
                "no_DDC_certificate",
            ]

            all_checking_field_OK = True
            for field in fields:
                if self.data.get(field) == "yes":
                    all_checking_field_OK = False
                    break
            if True == all_checking_field_OK:
                raise forms.ValidationError(_('all checking fields are qualified!'))
                return rectification_qualified

        return rectification_qualified

class ForkliftRepairForm(forms.ModelForm):
    owner = forms.ChoiceField(
            label=_('Owner'),
            choices = set((ins, ins) for ins in get_user_model().objects.all()),
            # widget=forms.RadioSelect(),
            required=True
            )           

    def __init__(self, *args, **kwargs):
        super(ForkliftRepairForm, self).__init__(*args, **kwargs)
        self.fields['repaire_date'].widget.attrs['disabled'] = True

    class Meta:
        model = ForkliftRepair

        exclude = {
            "inspector",
        }     

class ForkliftAnnualInspectionImageForm(forms.ModelForm):

    class Meta:
        model = ForkliftAnnualInspectionImage

        fields = ["image",]

        widgets = {
            'image': ImageFileInput(),
        }        