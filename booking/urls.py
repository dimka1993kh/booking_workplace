from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Workplace_.as_view(), name='booking'),
    path('all_booking/', views.all_booking, name='all_booking'),   
    path('<int:pk>', views.create_booking, name='workplace'),
    path('end_booking/', views.end_booking, name='end_booking'),
    path('<int:pk>/delete/', views.BookingDelete.as_view(), name='delete'),
]