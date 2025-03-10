from django.urls import path, include
from rest_framework import routers
from cliquentrega_app.users import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'users'

router = routers.DefaultRouter()
router.register(r'usuarios', views.UserViewSet, basename='usuarios')

urlpatterns = [
    path('', include(router.urls)),
    
    # Endpoints para Autenticação via JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Para login e obter token de acesso
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Para atualizar o token de acesso
]
