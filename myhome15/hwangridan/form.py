from django import forms
from hwangridan.models import Shop


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = "__all__"
