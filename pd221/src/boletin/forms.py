from django import forms

class RegForm(forms.Form):
	nombre = forms.CharField(max_lemght=100)
	edad = forms.IntegerField()