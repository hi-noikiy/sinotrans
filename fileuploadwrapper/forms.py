from django import forms

class UploadFileForm(forms.Form):
  image = forms.ImageField(widget=forms.FileInput(
    attrs={'required': 'required'}))  # required=True is the default, but not show it validation in template