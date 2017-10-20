from django import forms
from django.utils.translation import ugettext_lazy as _
from django.forms import BaseFormSet,BaseModelFormSet, formset_factory
from django.forms.models import modelformset_factory
from django.contrib.admin import widgets                                       
from django.forms.widgets import Media
from django.contrib.admin.templatetags.admin_static import static

from .models import (
    OfficeInspection,
    DailyInspection,
    shelf_inspection_record, shelf, shelf_inspection,
    equipment,ElectricalEquipmentInspection,SprayPumpRoomInspection
)

RESULT_OPTION = (
    ('yes', 'Yes'),
    ('no', 'No'),
)

class OfficeInspectionForm(forms.ModelForm):
    class Meta:
        model = OfficeInspection

        exclude = [
            'timestamp',
            'updated',
            'image'
        ]
        

    plug = forms.ChoiceField(
            choices=RESULT_OPTION,
            widget = forms.RadioSelect,
            )

    power = forms.ChoiceField(
            choices=RESULT_OPTION,
            widget = forms.RadioSelect,
            )
    # ModelChoiceField

    '''
    def clean_plug(self):
        return self.data.get('plug')
    '''

class DailyInspectionForm(forms.ModelForm):
    
    
    try: # may report error in fresh migrations from scratch
        impact = forms.MultipleChoiceField(
                label=_('Impact'),
                choices = lambda: (item for item in DailyInspection.daily_insepction_impact),
                widget = forms.SelectMultiple(),
                #widget=forms.CheckboxSelectMultiple(),
                initial = ['environment'],
                #initial= lambda: [item for item in DailyInspection.daily_insepction_impact if item],
                required=True
                )
    except:
        pass

    def __init__(self, *args, **kwargs):
        super(DailyInspectionForm, self).__init__(*args, **kwargs)
        self.fields['due_date'].widget = widgets.AdminDateWidget()

        for field in self.fields.values():
            if not field in self.Meta.exclude:
                field.widget.attrs={"class":"form-control"}

    def clear_image_after(self):
        if self.data.get('image_after-clear'):
            return "on"
        return None

    def clear_image_before(self):
        if self.data.get('image_before-clear'):
            return "on"
        return None

    class Meta:
        model = DailyInspection

        exclude = [
            'timestamp',
            'updated',
        ]
        
    class Media:
        css = {
            'all': ('admin/css/base.css','admin/css/forms.css','css/form_horizontal_layout.css',),
        }
        #js = ['js/form_horizontal_layout.js']


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

    # ModelChoiceField

class InspectionFilterForm(forms.Form):
    q = forms.CharField(label='Search', required=False)
    '''
    category_id = forms.ModelMultipleChoiceField(
        label='Category',
        queryset=Category.objects.all(), 
        widget=forms.CheckboxSelectMultiple, 
        required=False)
    '''

    category = forms.MultipleChoiceField(
            label=_('Category'),
            choices = DailyInspection.daily_insepction_category,
            #widget = forms.SelectMultiple(),
            widget=forms.CheckboxSelectMultiple(),
            initial = None,
            required=False
            )    

    rectification_status = forms.ChoiceField(
            label=_('Rectification Status'),
            choices = DailyInspection.daily_insepction_correction_status,
            widget=forms.RadioSelect(),
            required=False
            )   
    #owner = forms.CharField(label='Owner',required=False)
    try:
        owner = forms.ChoiceField(
                label=_('Owner'),
                choices = set((dailyinspection.owner,dailyinspection.owner) for dailyinspection in DailyInspection.objects.all()),
                widget=forms.RadioSelect(),
                initial = None,
                required=False
                )    
    except:
        pass

class shelf_inspection_Form(forms.ModelForm):
    class Meta:
        model = shelf_inspection

        exclude = [
        ]

class shelf_inspection_recordForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(shelf_inspection_recordForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.instance1 = instance
            #self.fields['shelf'].widget.attrs['readonly'] = True
            #self.fields['shelf'].widget.attrs['disabled'] = True
            #self.fields['use_condition'].empty_label = None

    def clean(self):
        #self.cleaned_data['shelf'] = self.clean_shelf()        
        self.cleaned_data['id'] = self.clean_id()
        #print self.cleaned_data
        return self.cleaned_data

    def clean_id(self):
        instance = getattr(self, 'instance', None)
        
        if instance and instance.id:
            return instance.id
        elif self.cleaned_data.get('id', None):
            return self.cleaned_data['id']
        else:
            id = self.data.get(self.prefix + '-id', None)
            return id

    def clean_shelf(self):
        instance = getattr(self, 'instance', None)
        
        if instance and instance.id:
            return instance.shelf
        elif self.cleaned_data.get('shelf', None):
            return self.cleaned_data['shelf']
        else:
            id = self.cleaned_data.get('id', None)
            if id:
                try:
                    shelf_inspection_record_instance = shelf_inspection_record.objects.get(pk=id)
                    return shelf_inspection_record_instance.shelf
                except:
                    return None
            else:
                return None


    class Meta:
        model = shelf_inspection_record

        exclude = [
            'shelf_inspection',
            'comments',
            'check_person',
            'forecast_complete_time',
        ]

        # workaround, not sure whether this function is already exist
        disabled = [
            #'shelf'
        ]

        hidden = [
            'id',
        ]

        hidden_form = [
            'shelf',
            'id',
        ]

class shelf_inspection_recordModelFormSet(BaseModelFormSet):
    def is_valid(self):
        return super(shelf_inspection_recordModelFormSet, self).is_valid()

shelf_inspection_record_Formset = modelformset_factory(shelf_inspection_record, 
                                            form=shelf_inspection_recordForm, 
                                            formset=shelf_inspection_recordModelFormSet, 
                                            extra=0)

class shelfFilterForm(forms.Form):

    is_gradient_measurement_mandatory = forms.BooleanField(
            label=_('Gradient Check Only'),
            required=False
            )

    try:
        type = forms.ChoiceField(
                label=_('Shelf Type'),
                choices = set((ins.type, ins.type) for ins in shelf.objects.all()),
                widget=forms.RadioSelect(),
                required=False
                )   

        CHOICE_LIST = []
        for ins in shelf.objects.all().order_by('warehouse'):
            if not (ins.warehouse, ins.warehouse) in CHOICE_LIST:
                CHOICE_LIST.append((ins.warehouse, ins.warehouse))
        CHOICE_LIST.sort()
        CHOICE_LIST.insert(0, ('', '----'))


        warehouse = forms.ChoiceField(
                label=_('Warehouse'),
                #choices = [(ins.warehouse, ins.warehouse) for ins in shelf.objects.all()].insert(0, ('', '----')) ,
                choices = CHOICE_LIST,
                widget=forms.Select(),
                initial = None,
                required=False
                )    

        CHOICE_LIST = []
        for ins in shelf.objects.all().order_by('compartment'):
            if not (ins.compartment, ins.compartment) in CHOICE_LIST:
                CHOICE_LIST.append((ins.compartment, ins.compartment))
        CHOICE_LIST.sort()
        CHOICE_LIST.insert(0, ('', '----'))

        compartment = forms.ChoiceField(
                label=_('Compartment'),
                choices = CHOICE_LIST,
                widget=forms.Select(),
                initial = None,
                required=False
                )  

        CHOICE_LIST = []
        for ins in shelf.objects.all().order_by('warehouse_channel'):
            if not (ins.warehouse_channel, ins.warehouse_channel) in CHOICE_LIST:
                CHOICE_LIST.append((ins.warehouse_channel, ins.warehouse_channel))
        CHOICE_LIST.sort()
        CHOICE_LIST.insert(0, ('', '----'))

        warehouse_channel = forms.ChoiceField(
                label=_('Warehouse Channel'),
                choices = CHOICE_LIST,
                widget=forms.Select(),
                initial = None,
                required=False
                ) 
    except:
        pass

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
        self.fields['equipment'].queryset = equipment.objects.filter(type='electrical equipment')

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

class SprayPumpRoomInspectionForm(forms.ModelForm):
    class Meta:
        model = SprayPumpRoomInspection

        exclude = {
            'month',
        }

spray_pumproom_inspection_model_formset = modelformset_factory(SprayPumpRoomInspection,
                                            form=SprayPumpRoomInspectionForm,
                                            extra=0)