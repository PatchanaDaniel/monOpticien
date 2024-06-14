from rest_framework.serializers import ModelSerializer as MS ,SerializerMethodField

from monOpticien.models import Client

class ClienSerializer(MS):
    class Meta:
        model=Client
        fields=['nom','prenom','motifs','date','heure']