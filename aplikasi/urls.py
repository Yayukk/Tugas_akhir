from django.urls import path
from . import views

urlpatterns = [
    path('aplikasi/', views.aplikasi, name='aplikasi'),
]