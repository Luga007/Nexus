from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class ProtectionOfDataView(APIView):
    permission_classes = (IsAuthenticated,)
