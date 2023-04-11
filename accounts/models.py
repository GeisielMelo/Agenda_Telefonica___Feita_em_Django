from django import forms
from django.db import models

from contatos.models import Contato


class FormContato(forms.ModelForm):
    class Meta:
        model = Contato
        exclude = ('mostrar',)
