
from .models import EmpRoutines
from .serializers import EmpRoutinesListSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate


class EmpRoutineAPI(generics.ListCreateAPIView):
    serializer_class = EmpRoutinesListSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = EmpRoutines.objects.filter(client = user)
        return queryset
