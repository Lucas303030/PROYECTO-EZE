# forms.py
from django import forms
from .models import Tracking

class TrackingForm(forms.ModelForm):
    class Meta:
        model = Tracking
        # Excluye campos que no deberían ser editables
        fields = ['pieza', 'origen', 'destino', 'estado']
