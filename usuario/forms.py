from django import forms

from usuario.models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext as _


class RegistrationForm(UserCreationForm):
    """
    Esta clase hereda de UserCreationForm
    UserCreationForm contiene usernamme, password1 y password2
    Se le agrega email

    """
    email = forms.EmailField(
        max_length=254,
        help_text="Campo obligatorio. Ingrese una direccion de correo valida.",
    )
    password1 = forms.CharField(
        label=_("Contraseña"), widget=forms.PasswordInput, help_text=_("Tu contraseña no puede ser similar a otra información personal. Debe contener al menos 8 caracteres. No puede ser una contraseña común. No puede ser completamente numérica.")
        )
    password2 = forms.CharField(
        label=_("Confirmar contraseña"), widget=forms.PasswordInput, help_text=_("Ingrese la misma contraseña para verificación.")
        )

    username = forms.CharField(label=_("Nombre de usuario"), max_length=150, help_text=_("Requerido. 150 caracteres o menos. Letras, dígitos y @/./+/-/_ solamente."))
    cliente = forms.BooleanField(initial=True)


    class Meta:
        model = Usuario
        fields = ("username", "email", "password1", "password2", "cliente")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    error_messages = {
        'password_mismatch': _("Las contraseñas no coinciden."),
        'password_too_short': _("La contraseña es demasiado corta."),
        'password_common': _("La contraseña no puede ser común."),
        'password_entirely_numeric': _("La contraseña no puede ser completamente numérica."),
        'username_exists': _("Este nombre de usuario ya está en uso."),
        'email_exists': _("Ya existe una cuenta con este correo electrónico."),
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].error_messages.update({
            'unique': self.error_messages['username_exists'],
        })
        self.fields['email'].error_messages.update({
            'unique': self.error_messages['email_exists'],
        })