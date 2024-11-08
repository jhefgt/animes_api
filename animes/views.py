from django.db.models import Count, Avg
from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from animes.models import Animes
from animes.serializers import AnimeSerializer, AnimeListDetailSerializer
from reviews.models import Review


class AnimeCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Animes.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AnimeListDetailSerializer
        return AnimeSerializer


class AnimeRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Animes.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AnimeListDetailSerializer
        return AnimeSerializer


class AnimeStatsView(views.APIView):
    permission_classe = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Animes.objects.all()

    def get(self, request):
        total_movies = self.queryset.count()
        animes_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']

        return response.Response(data={
            'total_moveis': total_movies,
            'movie_by_genre': animes_by_genre,
            'total_reviews': total_reviews,
            'average_stars': round(average_stars, 1) if average_stars else 0, }, status=status.HTTP_200_OK)
