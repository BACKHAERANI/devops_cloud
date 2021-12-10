from wannaone.models import Star
from django import forms


class StarForm(forms.ModelForm):
    class Meta:
        model = Star
        fields = '__all__'