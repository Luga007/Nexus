from django import forms
from .models import Product
from category.models import Category, Region


class ProductForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control input-md', 'placeholder': 'Add your title', 'label': 'title'})
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control input-md', 'placeholder': 'Add your description'})
    )

    price = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control input-md', 'placeholder': 'Add your price'})
    )
    created_at = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'class': 'form-control input-md', 'placeholder': 'Add your date', 'type': 'datetime-local'})
    )
    category = forms.ModelChoiceField(queryset=Category.objects.filter(is_main=True), widget=forms.Select(attrs={'class': 'tg-select form-control', 'label': 'Select category'}))

    brand = forms.ModelChoiceField(queryset=Product.objects.select_related('brand').all(), widget=forms.Select(attrs={'class': 'tg-select form-control', 'label': 'Select brand'}))

    location = forms.ModelChoiceField(queryset=Region.objects.all(), widget=forms.Select(attrs={'class': 'tg-select form-control', 'label': 'Select location'}))
    image = forms.ImageField()
    class Meta:
        model = Product
        exclude = ['created_at', 'updated_at', 'user', 'status']

