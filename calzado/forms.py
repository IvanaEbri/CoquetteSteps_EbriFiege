from django import forms
from .models import Calzado
from django.contrib import messages
from django.utils.translation import gettext as _

class CalzadoForm(forms.ModelForm):

    class Meta:
        model = Calzado
        fields = ['codigo', 'nombre', 'tipo_calzado', 'foto_prod', 'descripcion', 'color', 'material', 'precio']
        widgets = {
            'foto_prod': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.Select(attrs={'class': 'form-control'}),
            'material': forms.Select(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo_calzado': forms.Select(attrs={'class': 'form-control'}),
        }

    error_messages = {
        'code_exists': _("Este codigo de producto ya existe."),
        'name_exists': _("Este nombre de producto ya existe."),
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['codigo'].error_messages.update({
            'unique': self.error_messages['code_exists'],
        })
        self.fields['nombre'].error_messages.update({
            'unique': self.error_messages['name_exists'],
        })

class DeleteForm(forms.Form):
    confirm_delete = forms.BooleanField(label='Confirmar eliminación', required=True)