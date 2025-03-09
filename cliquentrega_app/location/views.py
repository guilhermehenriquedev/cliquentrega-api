from rest_framework import viewsets
from .models import Cidade
from .serializers import CidadeSerializer

# Create your views here.
class CidadeViewSet(viewsets.ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer