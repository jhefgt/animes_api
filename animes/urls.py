from django.urls import path
from . import views

urlpatterns = [
    path('animes/', views.AnimeCreateListView.as_view(), name='anime-list'),
    path('animes/<int:pk>/', views.AnimeRetriveUpdateDestroyView.as_view(), name='animes-detail-list'),
    path('animes/stats/', views.AnimeStatsView.as_view(), name='anime-stats-view'),
]
