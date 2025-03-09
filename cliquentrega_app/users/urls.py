from django.urls import path, include
from rest_framework import routers
from cliquentrega_app.users import views

app_name = 'users'

router = routers.DefaultRouter()
router.register(r'users', views.UsuarioViewSet, basename='users')


urlpatterns = [
    path(
        '', include(router.urls)
    ),
]
