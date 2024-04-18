from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
import pycountry


class UserRegistrationForm(UserCreationForm):
    COUNTRY_CODES = [(country.alpha_2, f"{country.alpha_2} ({country.name})") for country in pycountry.countries]

    phone_country_code = forms.ChoiceField(choices=COUNTRY_CODES)
    phone_number = forms.CharField(max_length=15)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'phone_country_code',
                  'phone_number' , 'profile_photo']



class UserLoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']



class CustomUserEditForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'phone_country_code', 'phone_number']

    def clean_password1(self):
        """
        Validate the password (if needed, you can add custom validation here)
        """
        password1 = self.cleaned_data.get('password1')
        return password1

    def save(self, commit=True):
        user = super().save(commit=False)
        password1 = self.cleaned_data.get('password1')
        if password1:
            user.set_password(password1)
        if commit:
            user.save()
        return user



class ApplyLeave(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)