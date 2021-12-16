from django import forms
from shop.models import Review, Shop


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = '__all__'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"