from django.shortcuts import render, redirect
from django.views.generic import View
from . import models, forms
import folium
import geocoder


class IndexView(View):
    """Представление реализации всей бизнес-логики"""

    template_name = 'app/index.html'

    def get(self, request):
        form = forms.NewAdForm()

        # Карта
        # map = folium.Map(zoom_start=2)

        ads = models.Advertisement.objects.all().order_by('-posted')
        # # Установка маркеров на карту по адресам кажого объявления
        # for ad in ads:
        #     location = geocoder.osm(ad.address)
        #     folium.Marker([location.lat, location.lng], tooltip=ad.address, popup=ad.title).add_to(map)

        # map = map._repr_html_()

        """Вывод объявлений при увеличении карты не знаю как реализовать, т.к. ранее не работал с картами
        и, соответственно, учился 'на ходу', чтобы выполнить задание. Алгоритм для реализации:
        1. Получить масштаб карты
        2. Получить все метки, которые входят в состав масштабирования
        3. Получить latitude и longitude каждой метки по циклу:
            3.1. Преобразовать координаты в адреса
            3.2. Отфильтровать все объявления по полученным адресам models.Advertsement.objects.filter(address=...)
        4. Вывести все полученные объявления."""

        return render(request, self.template_name, {
            'form': form,
            # 'map': map,
            'ads': ads,
        })

    def post(self, request):
        # Форма создания нового объявления
        form = forms.NewAdForm(request.POST, request.FILES)
        if form.is_valid():
            new_ad = form.save()
            new_ad.save()
            return redirect('/')


def google(request):
    return render(request, 'google2ad1c395f4f37380.html')