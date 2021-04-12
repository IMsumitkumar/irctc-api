from django.urls import path
from app import views

urlpatterns = [
    path('class-api/',views.CapiOverview, name="class-api-overview"),
    path('class-travel-data/', views.TravelList.as_view(), name='class-travel-list'),
    path('class-travel-details/<int:pk>/', views.TravelDetail.as_view(), name='class-travel-details'),
    
    
    path('func-api/',views.FapiOverview, name="func-api-overview"),
    path('func-travel-data/',views.travelList, name="func-travel-list"),
    path('func-travel-detail/<int:pk>/',views.travelDetail, name="func-travel-detail"),
    path('func-travel-create/',views.travelCreate, name="func-api-create"),
    path('func-travel-update/<int:pk>/',views.travelUpdate, name="func-api-update"),
    path('func-travel-delete/<int:pk>/',views.travelDelete, name="func-api-delete"),

]
