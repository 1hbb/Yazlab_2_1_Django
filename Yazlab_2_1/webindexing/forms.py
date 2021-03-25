from django import forms


class CalculateFrequentsForm(forms.Form):
    url = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter website url'}), label=False)


class KeywordsForm(forms.Form):
    url1 = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter website1 url'}), label=False)
    url2 = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter website2 url'}), label=False)


class IndexRank(forms.Form):
    url1 = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter website url'}), label=False)
    urls = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter website urls(www.example1.com,www.example1.com,.... )'}), label=False)
