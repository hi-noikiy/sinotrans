from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import AnnualTraningPlan
import datetime
from django.utils import timezone

class AnnualTraningPlanForm(forms.ModelForm):
    class Meta:
        model = AnnualTraningPlan

        exclude = {
        }

    def __init__(self, *args, **kwargs):
        super(AnnualTraningPlanForm, self).__init__(*args, **kwargs)
        self.fields['actual_date'].widget.attrs['disabled'] = True

class AnnualTrainingPlanFilterForm(forms.Form):

    year = forms.IntegerField(
        label=_('year'),
        #initial=datetime.datetime.now().year,
        min_value=2017,
        initial=timezone.now().year,        
        required=False)        