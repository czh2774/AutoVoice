from django import forms
from toolmodel.models import FootballWealthResolution


class FootballWealthResolutionForm(forms.ModelForm):
    long_desc = forms.CharField(widget=forms.Textarea(attrs={'cols': 10, 'rows': 20}))
    short_desc = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = FootballWealthResolution
        fields = ['content']
