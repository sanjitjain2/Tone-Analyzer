from django import forms

from .models import Tone


class ToneForm(forms.ModelForm):
	class Meta:
		model = Tone
		fields = [
			"content"
		]

		labels = {"content" : ""}