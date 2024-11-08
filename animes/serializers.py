from django.db.models import Avg
from rest_framework import serializers
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer
from animes.models import Animes


class AnimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Animes
        fields = '__all__'

    def validade_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError('Resumo não deve ser maior que 200 caracteres.')
        return value


class AnimeListDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genre = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Animes
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)

        return None
