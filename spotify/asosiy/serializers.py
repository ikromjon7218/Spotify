from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.utils.dateparse import parse_duration
from .models import *

class QoshiqchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qoshiqchi
        fields = '__all__'

class AlbomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albom
        fields = '__all__'

class QoshiqSerializer(serializers.Serializer):
    nom = serializers.CharField(max_length=100)
    janr = serializers.CharField(max_length=100)
    sana = serializers.DateField()
    fayl = serializers.FileField()
    davomiylik = serializers.DurationField()
    albom = serializers.PrimaryKeyRelatedField(queryset=Albom.objects.all(), allow_null=True)

    def validate_fayl(self, value):
        if value and not value.name[:-4] in '.mp3':
            raise ValidationError("Fayl ustuni .mp3 bilan tugamagan")
        return value

    def validate_davomiylik(self, value):
        davomiylik = parse_duration(value)
        if davomiylik.total_seconds() < 420:
            raise serializers.ValidationError("Davomiyligi 7 minutdan kam bo'lishi mumkin emas")
        return value

