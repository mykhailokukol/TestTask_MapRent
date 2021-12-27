from django.db import models


# Перечень типов помещений
HOUSE_TYPES = [
        ('house', 'дом'),
        ('apartments', 'апартаменты'),
        ('apartment', 'квартира'),
        ('room', 'комната'),
    ]


class Advertisement(models.Model):
    """Модель таблицы 'Объявление'"""

    # Текст объявление (название)
    title = models.CharField(max_length=128, null=False, blank=False, default='Сдам...')
    # Фото объявления
    photo = models.ImageField(upload_to='ads/', null=True, blank=True)
    # Тип помещения
    type = models.CharField(choices=HOUSE_TYPES, max_length=12, null=False, blank=False, default='квартира')
    # Стоимость
    price = models.IntegerField(null=False, blank=True, default=0)
    # Описание
    description = models.TextField(null=True, blank=True)
    # Адрес
    address = models.CharField(max_length=256, null=False, blank=False, default='Ukraine')

    posted = models.DateTimeField(auto_now_add=True, null=True)

    # Метод строчного вывода объекта класса (модели)
    def __str__(self):
        return self.title
