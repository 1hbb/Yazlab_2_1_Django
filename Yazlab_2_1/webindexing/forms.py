from django import forms


class CalculateFrequentsForm(forms.Form):
    url = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter website url'}), label=False)


class KeywordsForm(forms.Form):
    url1 = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter website url'}), label=False)
    url2 = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter website url'}), label=False)


class SimilarityForm(forms.Form):
    url1 = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter website url'}), label=False)
    url2 = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter website url'}), label=False)
