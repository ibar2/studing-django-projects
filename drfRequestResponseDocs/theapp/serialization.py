from rest_framework.serializers import ModelSerializer
from .models import snipet


class usersSerializer(ModelSerializer):
    class Meta:
        model = snipet
        fields = ['id', 'title', 'code', 'lineos', 'language', 'style']
