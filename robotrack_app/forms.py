from django import forms
from django.contrib.auth.models import User
import robotrack_app
from robotrack_app.models import Competition


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    username = forms.CharField(label='Login')
    email = forms.EmailField(label="Email", widget=forms.EmailInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class CompetitionForms(forms.ModelForm):
    class Meta:
        model = Competition
        fields = ['name']


class RefreeForms(forms.ModelForm):
    referee = forms.CharField(widget=forms.Select(choices=self.get_full_name()))

    def get_full_name(self):
        full_name = robotrack_app.models.User.objects.values('first_name', 'last_name')
        print('full_name', full_name)
        return full_name
