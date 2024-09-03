from rest_framework import serializers
from .models import despesas

class despesasSerializer(serializers.ModelSerializer):
    class Meta:
        model = despesas
        fields = '__all__'