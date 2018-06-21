from django import forms

from .models import Inmate

class InmateForm(forms.ModelForm):
    class Meta:
        model = Inmate
        fields = ('inmateNumber', 'lastName', 'firstName', 'caseTags')
