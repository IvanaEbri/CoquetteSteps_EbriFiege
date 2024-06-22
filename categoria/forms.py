from django import forms
from .models import Categoria, Tipo
from django.contrib import messages
from django.utils.translation import gettext as _

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ['categoria']
        widgets = {
            'categoria': forms.TextInput(attrs={'class': 'form-control'})
        }

    error_messages = {
        'category_exists': _("Esta categoria ya existe."),
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categoria'].error_messages.update({
            'unique': self.error_messages['category_exists'],
        })

class TipoForm(forms.ModelForm):

    class Meta:
        model = Tipo
        fields = ['tipo','categoria_nom']
        widgets = {
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria_nom': forms.Select(attrs={'class': 'form-control'})
        }

    error_messages = {
        'type_exists': _("Este tipo ya existe."),
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categoria_nom'].queryset = Categoria.objects.all()
        self.fields['tipo'].error_messages.update({
            'unique': self.error_messages['type_exists'],
        })

class DeleteForm(forms.Form):
    confirm_delete = forms.BooleanField(label='Confirmar eliminación', required=True)