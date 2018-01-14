from django import forms
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

class DashboardForm(forms.Form):
    year = forms.IntegerField(
        label=_('year'),
        initial=timezone.now().year,
        min_value=2000,
        required=False)    

    def clean_year(self):
        year = self.cleaned_data['year']
        if year:
            raise forms.ValidationError(_('This field is required.')) 

        return year

    def __init__(self, *args, **kwargs):
        super(DashboardForm, self).__init__(*args, **kwargs)
        self.fields['year'].widget.attrs['class'] ="form-control"
        self.fields['year'].widget.attrs['min'] ="2000"
        self.fields['year'].widget.attrs['max'] = timezone.now().year + 1