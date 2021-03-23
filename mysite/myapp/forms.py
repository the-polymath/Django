from django import forms

class NewList(forms.Form):
    name = forms.CharField(max_length=200, label="Name")
    check = forms.BooleanField(required=False)
