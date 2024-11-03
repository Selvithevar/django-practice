from django import forms

class Itemforms(forms.Form):
    name = forms.CharField()
    quantity = forms.IntegerField()