from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

from api.serializers import CareersSerializer
from core.models import Careers


class CareersViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    queryset = Careers.objects.all()
    serializer_class = CareersSerializer

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated()]
        return [AllowAny()]
