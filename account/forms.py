from django import forms
from .models import User

class UserCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta():
        model=User
        fields=('name', 'email', 'mobile', 'username', 'password', 'confirm_password')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            self.add_error('confirm_password', 'Password and confirm password does not matched.')
            # raise forms.ValidationError("Password and confirm password does not matched.")

        return cleaned_data
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")
        
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists.")
        
        return username
    
    def clean_mobile(self):
            mobile = self.cleaned_data.get('mobile')
            if User.objects.filter(mobile=mobile).exists():
                raise forms.ValidationError("Mobile already exists.")
            
            return mobile
