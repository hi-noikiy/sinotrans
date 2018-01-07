from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import AnnualTraningPlan, TrainingRecord, TrainingCourse
import datetime
from django.utils import timezone

class AnnualTraningPlanForm(forms.ModelForm):
    class Meta:
        model = AnnualTraningPlan

        exclude = {
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)

        super(AnnualTraningPlanForm, self).__init__(*args, **kwargs)
        self.fields['actual_date'].widget.attrs['disabled'] = True
        self.fields['year'].widget.attrs['disabled'] = True
        
        if self.request:
            course_class = self.request.GET.get("class") or self.request.session.get("course_class")
            self.fields['training_record'].queryset = TrainingRecord.objects.filter(training_course__training_class=course_class) if course_class else TrainingRecord.objects.all()
            self.fields['training_course'].queryset = TrainingCourse.objects.filter(training_class=course_class) if course_class else TrainingCourse.objects.all()

            self.fields['training_course'].empty_label = None

# class TransportationAnnualTraningPlanForm(AnnualTraningPlanForm):
#     course_class = "transportation"
#     training_record = forms.ModelChoiceField(
#             label=_('training record'),
#             queryset=TrainingRecord.objects.filter(training_course__training_class=course_class) if course_class else TrainingRecord.objects.all(),
#             # empty_label = None, 
#             required=True
#             )

    
# class WarehouseAnnualTraningPlanForm(AnnualTraningPlanForm):
#     course_class = "warehouse"
#     training_record = forms.ModelChoiceField(
#             label=_('training record'),
#             queryset=TrainingRecord.objects.filter(training_course__training_class=course_class) if course_class else TrainingRecord.objects.all(),
#             # empty_label = None, 
#             required=True
#             )

class AnnualTrainingPlanFilterForm(forms.Form):

    year = forms.IntegerField(
        label=_('year'),
        #initial=datetime.datetime.now().year,
        min_value=2017,
        initial=timezone.now().year,        
        required=False)        


class TrainingRecordForm(forms.ModelForm):
    class Meta:
        model = TrainingRecord

        exclude = {
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)

        super(TrainingRecordForm, self).__init__(*args, **kwargs)
        
        if self.request:
            course_class = self.request.GET.get("class") or self.request.session.get("course_class")
            self.fields['training_course'].queryset = TrainingCourse.objects.filter(training_class=course_class) if course_class else TrainingCourse.objects.all()
            self.fields['training_course'].empty_label = None    