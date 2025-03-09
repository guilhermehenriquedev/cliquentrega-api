from django.urls import path, include
from rest_framework import routers
from cliquentrega_app.location import views

app_name = 'location'

router = routers.DefaultRouter()
router.register(r'city', views.CidadeViewSet, basename='city')

urlpatterns = [
    path(
        '', include(router.urls)
    ),
]
