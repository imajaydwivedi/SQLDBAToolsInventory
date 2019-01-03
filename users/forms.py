from django import forms
from django.contrib.auth.models import User
from users.models import UserProfileInfo
from django.core import validators


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    # class Meta():
    #     model = User
    #     fields = ('username', 'password')


def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name should start with letter Z")


class FormName(forms.Form):
    # name = forms.CharField(validators=[check_for_z])
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Confirm Email")
    # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[
    #                              validators.MaxLengthValidator(0)])
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']
        if email != vemail:
            raise validators.ValidationError("MAKE SURE EMAILS MATCH!")

    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOTCHA BOT!")
    #     return botcatcher
