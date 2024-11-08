from django.urls import path
from . import views

urlpatterns = [
    path('actors/', views.ActorCreateListView.as_view(), name='actor-list'),
    path('actors/<int:pk>/', views.ActorRetriveUpdateDestroyView.as_view(), name='actor-detail-list'),
]
