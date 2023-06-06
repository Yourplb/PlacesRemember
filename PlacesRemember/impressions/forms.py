from django import forms
from .models import Impressions
from location_field.forms.plain import PlainLocationField


class ImpressionsForm(forms.ModelForm):
    class Meta:
        model = Impressions
        fields = ('title', 'description', 'location')
        location = PlainLocationField(based_fields=['title'], zoom=7, verbose_name='Местоположение')

        labels = {
            'title': False,
            'description': False,
            'location': False,
        }

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Название места',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Введите ваши впечатления',
                'rows': 6,
            }),
            'location': forms.TextInput(attrs={
                'placeholder': 'Местоположение',
                'data-map-type': 'roadmap',
                'class': 'location-input',
            }),
        }
