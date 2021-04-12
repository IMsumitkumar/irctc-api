from django.urls import path
from app import views

urlpatterns = [
    path('',views.apiOverview, name="api-overview"),
    path('travel-data/', views.TravelList.as_view(), name='travel-list'),
    path('travel-details/<int:pk>/', views.TravelDetail.as_view(), name='travel-details'),
]
