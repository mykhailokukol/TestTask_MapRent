from . import views
from rest_framework.routers import DefaultRouter


app_name = 'drf'

router = DefaultRouter()
router.register(r'ads', views.AdViewSet)