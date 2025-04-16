from django import forms


class EmailForm(forms.Form):
    to_email = forms.EmailField(label='Send To', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message...'}))
