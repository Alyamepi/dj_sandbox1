from django import forms

class AskNumber(forms.Form):
    n1 = forms.IntegerField(label = 'Enter a number')
    # by making it an IntegerField, the browser doesn't take any other input
    