from django import forms
from authwrapper.models import MyUser


#from django.forms.extras.widgets import SelectDateWidget
from django.contrib.admin import widgets
class MyUserForm(forms.ModelForm):
    #birthday = forms.DateField(widget=SelectDateWidget())
    #birthday = forms.DateField(widget=forms.SelectDateWidget) # availabe in django 1.9

    #first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'})) 
    
    class Meta:
        model = MyUser

        fields = [
            'first_name',
            'last_name',
            'nickname',
            'birthday',
            'sex',
            'image'
        ]

        """
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
        }
        """

    def __init__(self, *args, **kwargs):
        super(MyUserForm, self).__init__(*args, **kwargs)
        self.fields['sex'].empty_label = None     
        self.fields['birthday'].widget = widgets.AdminDateWidget()   

        for field in self.Meta.fields:
             self.fields[field].widget.attrs={"class":"form-control"}

        

    def clean_image(self):
        if self.cleaned_data.get("image") != None:
            return self.cleaned_data.get("image")
        elif self.data.get("image") == None:    
            raise forms.ValidationError("image can't be empty.")
        else:
            self.cleaned_data['image'] = self.data.get("image")
            return self.data.get("image")

'''
class UploadFileForm(forms.Form):
  image = forms.ImageField(widget=forms.FileInput(
    attrs={'required': 'required'}))  # required=True is the default, but not show it validation in template
'''    