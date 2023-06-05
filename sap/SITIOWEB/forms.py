from django import forms
from personas.models import persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = persona
        fields = ['nombre_completo','identificacion','celular','correo_electronico', 'nombre_evento', 'tipo_boleto']

