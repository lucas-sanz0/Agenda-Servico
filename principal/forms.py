from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CadastroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True, label='E-mail')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.fields:
            self.fields[campo].widget.attrs['class'] = 'form-control' 
