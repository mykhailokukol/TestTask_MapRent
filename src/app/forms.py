from django import forms
from . import models


class NewAdForm(forms.ModelForm):
    """Форма создания нового объекта модели..."""

    class Meta:
        """...где модель - 'Объявление'"""
        model = models.Advertisement
        fields = '__all__'
        labels = {
            'title': 'Название',
            'photo': 'Фото',
            'type': 'Тип помещения',
            'price': 'Цена',
            'description': 'Описание',
            'address': 'Адрес',
        }
        widgets = {
            'type': forms.Select(choices=models.HOUSE_TYPES),
        }