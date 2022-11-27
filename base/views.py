from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Persona
from .forms import PersonaCreateForm, PersonaUpdateForm


# Create your views here.
class PersonaListView(ListView):
    model = Persona

class PersonaCreateView(CreateView):
    model = Persona
    form_class = PersonaCreateForm

class PersonaUpdateView(UpdateView):
    model = Persona
    form_class = PersonaUpdateForm