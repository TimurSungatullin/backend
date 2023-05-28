from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from entity.models import Project
from entity.serializers import ProjectSerializer


class EntityViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
