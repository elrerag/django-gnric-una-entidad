from django.contrib import admin
from django.urls import path, include
from .views import PersonaListView, PersonaCreateView

application = "base"

urlpatterns = [
    path('persona/', PersonaListView.as_view(), name="persona_list"),
    path('persona/add', PersonaCreateView.as_view(), name="persona_create"),
]
