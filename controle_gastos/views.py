from django.shortcuts import render
from rest_framework import viewsets
from .models import despesas
from .serializers import despesasSerializer

class despesasViewSet(viewsets.ModelViewSet):
    queryset = despesas.objects.all()
    serializer_class = despesasSerializer


