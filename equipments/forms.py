from django import forms
from django.forms.models import modelformset_factory

from .models import (
    Equipment, EquipmentType, ElectricalEquipmentInspection,
)

class ElectricalEquipmentInspectionForm(forms.ModelForm):
    use_condition = forms.ChoiceField(
        choices=ElectricalEquipmentInspection.equipment_use_condition,
        widget=forms.RadioSelect,
    )

    class Meta:
        model = ElectricalEquipmentInspection

        exclude = {
        }

    def __init__(self, *args, **kwargs):
        super(ElectricalEquipmentInspectionForm, self).__init__(*args, **kwargs)
        #self.fields['equipment'].queryset = Equipment.objects.filter(type=EquipmentType(name='Electronic'))


        for field in self.fields.values():
            if not field in self.Meta.exclude:
                if 'class' in field.widget.attrs.keys():
                    field.widget.attrs['class'] = field.widget.attrs['class'] + ' form-control'
                else:
                    field.widget.attrs['class'] = 'form-control'

        self.fields['date_of_inspection'].widget.attrs['class'] = self.fields['date_of_inspection'].widget.attrs['class'] + ' calendar'

        # self.fields['use_condition'].choices = ElectricalEquipmentInspection.equipment_use_condition
        # self.fields['use_condition'].widget = forms.RadioSelect

    # def clean(self, *args, **kwargs):
    #     super(ElectricalEquipmentInspectionForm, self).clean(*args, **kwargs)
    #     equip = self.cleaned_data.get('equipment')
    #     date_of_inspection = self.cleaned_data.get('date_of_inspection')
    #     if self.Meta.model.objects.filter(equipment=equip, date_of_inspection=date_of_inspection).exists():
    #         raise forms.ValidationError('record already exist')

# class ElectricalEquipmentInspectionModelFormSet(BaseModelFormSet):
#     pass

electrical_equipment_inspection_model_formset = modelformset_factory(ElectricalEquipmentInspection,
                                            form=ElectricalEquipmentInspectionForm,
                                            #formset=ElectricalEquipmentInspectionModelFormSet,
                                            extra=1)