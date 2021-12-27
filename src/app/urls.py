from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index_page'),
    path('google2ad1c395f4f37380.html', views.google, name='google_page'),
]