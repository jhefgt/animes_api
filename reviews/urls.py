from django.urls import path
from . import views


urlpatterns = [
    path('review/', views.ReviewCreateListView.as_view(), name='review-list'),
    path('review/<int:pk>/', views.ReviewRetriveUpdateDestroyView.as_view(), name='review-detail-list')
]
