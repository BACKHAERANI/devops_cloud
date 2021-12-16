from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields =["username", "email"]

class LoginForm(AuthenticationForm):
    answer = forms.CharField(label="답을 맞춰줘!", help_text="3+3=?",)

    def clean_answer(self):
        answer = self.cleaned_data.get("answer")
        if answer != '6':
            raise forms.ValidationError("땡! 왜 이것도 몰라!")
        return answer

