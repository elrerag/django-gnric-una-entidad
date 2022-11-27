from django.forms import ModelForm

from .models import Persona

class PersonaCreateForm(ModelForm):
    class Meta:
        model = Persona
        fields = ("nombre",)

class PersonaUpdateForm(ModelForm):
    class Meta:
        model = Persona
        fields = ("nombre",)
