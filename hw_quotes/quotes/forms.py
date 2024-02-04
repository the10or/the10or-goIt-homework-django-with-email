from django import forms

from .models import Author, Quote, Tag


class AuthorForm(forms.ModelForm):
    fullname = forms.CharField(max_length=100)
    born_date = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    born_location = forms.CharField(max_length=100)

    class Meta:
        model = Author
        fields = ["fullname", "born_date", "born_location", "description"]


class QuoteForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'selectpicker'}),
        label="Choose tags"

    )

    author = forms.ModelChoiceField(
        queryset=Author.objects.all(),
        widget=forms.Select(attrs={'class': 'selectpicker'}),
        label="Choose author")

    text = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}),
        label="Quote text"
    )

    class Meta:
        model = Quote
        fields = ["text", "author", "tags"]
