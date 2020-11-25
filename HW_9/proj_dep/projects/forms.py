from django import forms
from .models import Staff, Project,Role
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# класс форм, не связанных с моделью
class ContactForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    def form_valid(self, form):
        # print(form.cleaned_data)
        return super().form_valid(form)


class StaffForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Staff
        exclude = ('user',)


class ProjectForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.TextInput()

    class Meta:
        model = Project
        exclude = ('user',)

class RoleForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Role
        exclude = ('user',)

class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your password',
    }))

    class Meta:
        model = User
        # fields = '__all__'
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {'username' : forms.TextInput(attrs={'placeholder':'John Gault', 'class':'col-md-12form-control'}),
                   'email' : forms.EmailInput(attrs={'placeholder':'your@mail.com', 'class':'col-md-12form-control'}),
                   }


class LoginForm(AuthenticationForm):
    class Meta:
        fields = '__all__'
