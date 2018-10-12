from django import forms

class AskNumber(forms.Form):
    n1 = forms.CharField(label = 'Enter a number', max_length=10)
    