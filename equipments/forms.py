from django import forms
from django.forms.models import modelformset_factory
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import widgets                                       
from django.forms.widgets import Media
from django.contrib.admin.templatetags.admin_static import static
from django.db.models.fields import BLANK_CHOICE_DASH

from .models import (
    AbstractEquipmentInspection, Equipment, EquipmentType, EquipmentInspection,
    SprayPumpRoomInspection,
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


class SprayPumpRoomInspectionForm(forms.ModelForm):
    class Meta:
        model = SprayPumpRoomInspection

        exclude = {
            'year',
            'month',
        }

spray_pumproom_inspection_model_formset = modelformset_factory(SprayPumpRoomInspection,
                                            form=SprayPumpRoomInspectionForm,
                                            extra=0)

class EquipmentInspectiontFilterForm(forms.Form):
    category_id = forms.ModelChoiceField(
        label='Category',
        queryset=EquipmentType.objects.all(), 
        widget=forms.Select(), 
        required=False)

    use_condition = forms.ChoiceField(
            label=_('Use Condition'),
            choices = BLANK_CHOICE_DASH + AbstractEquipmentInspection.equipment_use_condition,
            widget=forms.Select(),
            required=False
            ) 

    try:
        inspector = forms.ChoiceField(
                label=_('Inspector'),
                choices = BLANK_CHOICE_DASH + dict(set((equipment_inspection.inspector, equipment_inspection.inspector) for equipment_inspection in EquipmentInspection.objects.all())),
                widget=forms.Select(),
                initial = None,
                required=False
                )    
    except:
        pass

    date_of_inspection_start = forms.DateField(required=False)
    date_of_inspection_end = forms.DateField(required=False)

    def __init__(self, *args, **kwargs):
        super(EquipmentInspectiontFilterForm, self).__init__(*args, **kwargs)
        self.fields['date_of_inspection_start'].widget = widgets.AdminDateWidget()    
        self.fields['date_of_inspection_end'].widget = widgets.AdminDateWidget()    

    class Media:
        css = {
            'all': ('admin/css/base.css','admin/css/forms.css',),
        }

    #inherit from BaseForm
    @property
    def media(self):
        """
        Provide a description of all media required to render the widgets on this form
        """        
        media = Media(js=[static('js/jquery.init.both.js'), '/admin/jsi18n/', static('admin/js/core.js')])
        for field in self.fields.values():
            for item in field.widget.media._js:
                if not item.split('/')[-1] in ''.join(media._js):
                    media = media + Media(js=[item])

        media = media + Media(self.Media)

        return media        