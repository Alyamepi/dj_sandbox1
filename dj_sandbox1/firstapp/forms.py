from django import forms

class AskNumber(forms.Form):
    n1 = forms.IntegerField(label = 'Enter a number')
    