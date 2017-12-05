from django import forms
from django.utils.translation import ugettext_lazy as _
from django.forms import BaseFormSet,BaseModelFormSet, formset_factory
from django.forms.models import modelformset_factory
from django.contrib.admin import widgets                                       
from django.forms.widgets import Media
from django.contrib.admin.templatetags.admin_static import static
from django.conf import settings
from django.contrib.auth import get_user_model

from .models import (
    OfficeInspection,
    DailyInspection,
    shelf_inspection_record, shelf, shelf_inspection,
    
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

"""
from django.forms import MultipleChoiceField

class SchedulerProfileChoiceField(MultipleChoiceField):
    def label_from_instance(self, obj):
        return "%s %s" % (obj.category, obj.inspection_content)
"""

# https://docs.djangoproject.com/en/1.3/ref/forms/fields/#django.forms.ModelChoiceField
# https://docs.djangoproject.com/en/1.3/ref/forms/fields/#modelmultiplechoicefield

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

        owner = forms.ModelChoiceField(
                label=_('Owner'),
                queryset=get_user_model().objects.all(),
                empty_label = None, #not show enmpty
                required=True
                )         
        
   
    except:
        pass

    def __init__(self, *args, **kwargs):
        super(DailyInspectionForm, self).__init__(*args, **kwargs)
        self.fields['due_date'].widget = widgets.AdminDateWidget()

        for field in self.fields.values():
            if not field in self.Meta.exclude:
                if 'class' in field.widget.attrs.keys():
                    field.widget.attrs['class'] = field.widget.attrs['class'] + ' form-control'
                else:
                    field.widget.attrs['class'] = 'form-control'

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
            'rectification_status',
            'inspector',
            'completed_time'
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
    q = forms.CharField(label=_('Search'), required=False)

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

    # overdue = forms.BooleanField(
    #         label=_('Overdue'),
    #         # widget=forms.RadioSelect(),
    #         required=False
    #         )   

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

    start = forms.DateField(label=_("Date of Inspection Start"), required=False)
    end = forms.DateField(label=_("Date of Inspection End"), required=False)    

    def __init__(self, *args, **kwargs):
        super(InspectionFilterForm, self).__init__(*args, **kwargs)
        self.fields['start'].widget.attrs['class'] ="calenda"
        self.fields['end'].widget.attrs['class'] ="calenda"

class ShelfInspectionForm(forms.ModelForm):
    class Meta:
        model = shelf_inspection

        exclude = [
        ]

class ShelfGradientInspectionForm(forms.ModelForm):
    class Meta:
        model = shelf_inspection_record

        fields = [
            "gradient",
        ]
shelf_gradient_inspection_Formset = modelformset_factory(shelf_inspection_record, 
                                            form=ShelfGradientInspectionForm, 
                                            formset=BaseModelFormSet, 
                                            extra=0)

class ShelfInspectionRecordForm(forms.ModelForm):

    gradient = forms.DecimalField(
            label=_('Gradient'),
            min_value=-1.5,
            max_value=1.5,
            required=False
            )
    
    def __init__(self, *args, **kwargs):
        super(ShelfInspectionRecordForm, self).__init__(*args, **kwargs)
        
        self.fields['gradient'].widget.attrs['step'] = 0.1

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

        hidden = [ # input hiden, but still need the value for validation
            'id',
            'shelf',
        ]

        display_with_field_hiden = [
            'shelf',        
        ]

        field_display = [
            'use_condition',
            'is_locked'
        ]        

class shelf_inspection_recordModelFormSet(BaseModelFormSet):
    def is_valid(self):
        return super(shelf_inspection_recordModelFormSet, self).is_valid()

shelf_inspection_record_Formset = modelformset_factory(shelf_inspection_record, 
                                            form=ShelfInspectionRecordForm, 
                                            formset=shelf_inspection_recordModelFormSet, 
                                            extra=0)

class ShelfFilterForm(forms.Form):

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


class ShelfUploadForm(forms.Form):
    excel = forms.FileField(
                label=_('shelf upload'),
                required=False
                )   