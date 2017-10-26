from django import forms
from django.forms.models import modelformset_factory
from django.utils.translation import ugettext_lazy as _

from .models import (
    Equipment, EquipmentType, EquipmentInspection,
)

class EquipmentInspectionForm(forms.ModelForm):
    use_condition = forms.ChoiceField(
    	label=_('Use Condition'),
        choices=EquipmentInspection.equipment_use_condition,
        #widget=forms.RadioSelect,
        widget=forms.Select,
    )

    class Meta:
        model = EquipmentInspection

        exclude = {
        }

    def __init__(self, *args, **kwargs):
        super(EquipmentInspectionForm, self).__init__(*args, **kwargs)
         
        #self.fields['equipment'].queryset = Equipment.objects.filter(type__id=kwargs.get('cat',None))


        for field in self.fields.values():
            if not field in self.Meta.exclude:
                if 'class' in field.widget.attrs.keys():
                    field.widget.attrs['class'] = field.widget.attrs['class'] + ' form-control'
                else:
                    field.widget.attrs['class'] = 'form-control'

        self.fields['date_of_inspection'].widget.attrs['class'] = self.fields['date_of_inspection'].widget.attrs['class'] + ' calendar'

        # self.fields['use_condition'].choices = EquipmentInspection.equipment_use_condition
        # self.fields['use_condition'].widget = forms.RadioSelect

    # def clean(self, *args, **kwargs):
    #     super(EquipmentInspectionForm, self).clean(*args, **kwargs)
    #     equip = self.cleaned_data.get('equipment')
    #     date_of_inspection = self.cleaned_data.get('date_of_inspection')
    #     if self.Meta.model.objects.filter(equipment=equip, date_of_inspection=date_of_inspection).exists():
    #         raise forms.ValidationError('record already exist')

# class EquipmentInspectionModelFormSet(BaseModelFormSet):
#     pass

equipment_inspection_model_formset = modelformset_factory(EquipmentInspection,
                                            form=EquipmentInspectionForm,
                                            #formset=EquipmentInspectionModelFormSet,
                                            extra=1)