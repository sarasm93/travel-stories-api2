from django.urls import path
from destinations import views


urlpatterns = [
    path('destinations/', views.DestinationList.as_view()),
    path('destinations/<int:pk>/', views.DestinationDetail.as_view())
]
