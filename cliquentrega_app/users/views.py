from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import UserSerializer

Usuario = get_user_model()  # Obtém o modelo de usuário definido no AUTH_USER_MODEL

class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar usuários do sistema.
    """
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['post'])
    def create_user(self, request):
        """
        Endpoint para criar um novo usuário.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "Usuário criado com sucesso!", "user": UserSerializer(user).data}, status=201)
        return Response(serializer.errors, status=400)

    @action(detail=True, methods=['put'])
    def update_user(self, request, pk=None):
        """
        Endpoint para atualizar um usuário existente.
        """
        try:
            user = Usuario.objects.get(pk=pk)
        except Usuario.DoesNotExist:
            return Response({"error": "Usuário não encontrado."}, status=404)

        serializer = self.get_serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Usuário atualizado com sucesso!", "user": serializer.data})
        return Response(serializer.errors, status=400)

    @action(detail=True, methods=['delete'])
    def delete_user(self, request, pk=None):
        """
        Endpoint para deletar um usuário existente.
        """
        try:
            user = Usuario.objects.get(pk=pk)
            user.delete()
            return Response({"message": "Usuário deletado com sucesso!"}, status=204)
        except Usuario.DoesNotExist:
            return Response({"error": "Usuário não encontrado."}, status=404)
