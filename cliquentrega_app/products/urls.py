from django.urls import path, include
from rest_framework import routers
from cliquentrega_app.products import views

app_name = 'products'

router = routers.DefaultRouter()
router.register(r'products', views.ProdutoViewSet, basename='products')
router.register(r'categories', views.CategoriaViewSet, basename='categories')
router.register(r'flags', views.FlagViewSet, basename='flags')


urlpatterns = [
    path(
        '', include(router.urls)
    ),
]
