from django import forms
from .models import Crowdfunding

Crowdfunding_TYPE = (
	('health', 'Health'),
	('school', 'School'),
)

class CrowdfundingCreateForm(forms.ModelForm):
	class Meta:
		model = Crowdfunding

		exclude = [
			'is_favorite',
			'user',
		]

	category = forms.ChoiceField(
		choices = Crowdfunding_TYPE,
		widget = forms.RadioSelect,
		# empty_label = None,
		)

# class ProductImageForm(forms.ModelForm):
# 	class Meta:
# 		model = ProductImage
# 		fields = [
# 			'image',
# 			# 'product'
# 		]

# 	def clean_image(self):
# 		if self.cleaned_data.get("image") != None:
# 			return self.cleaned_data.get("image")
# 		elif self.data.get("image") == None:	
# 			raise forms.ValidationError("image can't be empty.")
# 		else:
# 			self.cleaned_data['image'] = self.data.get("image")
# 			return self.data.get("image")

# 	def is_valid(self):
# 		if self.clean_image != None:
# 			return True
# 		return False		