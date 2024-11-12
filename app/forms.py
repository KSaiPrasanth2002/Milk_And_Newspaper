from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserRegistration

class RegistrationForm(UserCreationForm):
    error_messages = {
        'duplicate_username': "This username is already taken.",
        'password_too_similar_to_last_name': "The password is too similar to the last name.",
    }

    class Meta(UserCreationForm.Meta):
        model = UserRegistration
        fields = ['username', 'first_name', 'last_name', 'email', 'city', 'address', 'pincode', 'phoneNumber']
        widgets = {
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            UserRegistration._default_manager.get(username=username)
        except UserRegistration.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )

    def clean_password2(self):
        password2 = self.cleaned_data.get("password2")
        last_name = self.cleaned_data.get("last_name")

        if last_name and password2 and password2.lower().startswith(last_name.lower()):
            raise forms.ValidationError(
                self.error_messages['password_too_similar_to_last_name'],
                code='password_too_similar_to_last_name',
            )
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = ['username', 'email', 'first_name', 'last_name', 'city', 'address', 'pincode', 'phoneNumber']
