from django import forms
from django.forms.models import modelformset_factory
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import widgets                                       
from django.forms.widgets import Media
from django.contrib.admin.templatetags.admin_static import static
from django.db.models.fields import BLANK_CHOICE_DASH

from .models import (
    AbstractEquipmentInspection, 
    Equipment, 
    EquipmentType, 
    EquipmentInspection,

    SprayPumpRoomInspection, 
    SprayWarehouseInspection,

    HSSEKPI,
)

from django.conf import settings
from django.contrib.auth import get_user_model

class EquipmentInspectionForm(forms.ModelForm):
    use_condition = forms.ChoiceField(
    	label=_('Use Condition'),
        choices=BLANK_CHOICE_DASH + EquipmentInspection.equipment_use_condition,
        #widget=forms.RadioSelect,
        widget=forms.Select,
    )

    try:
        owner = forms.ModelChoiceField(
                label=_('Owner'),
                queryset=get_user_model().objects.all(),
                empty_label = None, #not show enmpty
                required=True
                )     
    except:
        pass

    class Meta:
        model = EquipmentInspection

        exclude = {
            'inspector',
            'completed_time'
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

        self.fields['due_date'].widget.attrs['class'] = self.fields['due_date'].widget.attrs['class'] + ' calendar'

# class EquipmentInspectionModelFormSet(BaseModelFormSet):
#     pass

equipment_inspection_model_formset = modelformset_factory(EquipmentInspection,
                                            form=EquipmentInspectionForm,
                                            #formset=EquipmentInspectionModelFormSet,
                                            extra=1)




class EquipmentInspectiontFilterForm(forms.Form):
    category_id = forms.ModelChoiceField(
        label=_('Category'),
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

    date_of_inspection_start = forms.DateField(label=_("Date of Inspection Start"), required=False)
    date_of_inspection_end = forms.DateField(label=_("Date of Inspection End"), required=False)


    def __init__(self, *args, **kwargs):
        super(EquipmentInspectiontFilterForm, self).__init__(*args, **kwargs)
        self.fields['date_of_inspection_start'].widget.attrs['class'] ="calenda"
        self.fields['date_of_inspection_end'].widget.attrs['class'] ="calenda"

    '''        
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
    '''

class SprayPumpRoomInspectionForm(forms.ModelForm):

    try: 
        owner = forms.ModelChoiceField(
                label=_('Owner'),
                queryset=get_user_model().objects.all(),
                empty_label = None, #not show enmpty
                required=True
                )
    except:
        pass

    class Meta:
        model = SprayPumpRoomInspection

        exclude = {
            #'year',
            #'month',
            'inspector',
            'rectification_status',
        }

    def __init__(self, *args, **kwargs):
        super(SprayPumpRoomInspectionForm, self).__init__(*args, **kwargs)
        self.fields['year'].widget.attrs['readonly'] = True
        self.fields['month'].widget.attrs['readonly'] = True
        # if 'class' in self.fields['date_of_inspection'].widget.attrs.keys():
        #     self.fields['date_of_inspection'].widget.attrs['class'] = self.fields['date_of_inspection'].widget.attrs['class'] + "calenda"   
        # else:
        #     self.fields['date_of_inspection'].widget.attrs['class'] ="calenda"

spray_pumproom_inspection_model_formset = modelformset_factory(SprayPumpRoomInspection,
                                            form=SprayPumpRoomInspectionForm,
                                            extra=0)

class SprayWarehouseInspectionForm(forms.ModelForm):
    try: 
        owner = forms.ModelChoiceField(
                label=_('Owner'),
                queryset=get_user_model().objects.all(),
                empty_label = None, #not show enmpty
                required=True
                )
    except:
        pass

    class Meta:
        model = SprayWarehouseInspection

        exclude = {
            'inspector',
            'rectification_status',
        }

    def __init__(self, *args, **kwargs):
        super(SprayWarehouseInspectionForm, self).__init__(*args, **kwargs)
        self.fields['year'].widget.attrs['readonly'] = True

spray_warehouse_inspection_model_formset = modelformset_factory(SprayWarehouseInspection,
                                            form=SprayWarehouseInspectionForm,
                                            extra=0)

class HSSEKPIForm(forms.ModelForm):
    class Meta:
        model = HSSEKPI

        exclude = {
            'inspector',
        }

    def __init__(self, *args, **kwargs):
        super(HSSEKPIForm, self).__init__(*args, **kwargs)
        self.fields['year'].widget.attrs['readonly'] = True
        self.fields['month'].widget.attrs['readonly'] = True

hssekpi_model_formset = modelformset_factory(HSSEKPI,
                                            form=HSSEKPIForm,
                                            extra=0)

class SprayInspectionFilterForm(forms.Form):

    year = forms.IntegerField(
        label=_('year'),
        initial=2017,
        min_value=2000,
        required=False)