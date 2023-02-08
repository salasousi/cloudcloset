from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mycloset/', views.closet_index, name='index'),
]