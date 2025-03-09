from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('location/', include('cliquentrega_app.location.urls')),
    path('products/', include('cliquentrega_app.products.urls')),
    path('users/', include('cliquentrega_app.users.urls')),
    
]
