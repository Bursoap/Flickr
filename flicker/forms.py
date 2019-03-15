from django import forms


class FlickerForm(forms.Form):
    search = forms.CharField(max_length=255, required=True)
