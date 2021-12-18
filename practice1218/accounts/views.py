from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, TemplateView

signup = CreateView.as_view(form_class=UserCreationForm, template_name='accounts/sign.html')

login = LoginView.as_view(template_name='accounts/login.html')

logout = LogoutView.as_view(next_page='practice1218/root.html')

profile = login_required(TemplateView.as_view(template_name='accounts/profile.html'))

