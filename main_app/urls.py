from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mycloset/', views.closet_index, name='index'),
    path('mycloset/tops/<int:top_id>/', views.tops_detail, name='t_detail'),
    path('mycloset/bottoms/<int:bottom_id>/', views.bottoms_detail, name='b_detail'),
    path('mycloset/coats/<int:coat_id>/', views.coats_detail, name='c_detail'),
    path('mycloset/shoes/<int:shoe_id>/', views.shoes_detail, name='s_detail'),
    path('mycloset/accessories/<int:accessory_id>/', views.accessories_detail, name='a_detail'),
    path('mycloset/tops/<int:top_id>/add_top_photo/', views.add_top_photo, name='add_top_photo'),
    path('mycloset/bottoms/<int:bottom_id>/add_bottom_photo/', views.add_bottom_photo, name='add_bottom_photo'),
    path('mycloset/coats/<int:coat_id>/add_coat_photo/', views.add_coat_photo, name='add_coat_photo'),
    path('mycloset/shoes/<int:shoe_id>/add_shoe_photo/', views.add_shoe_photo, name='add_shoe_photo'),
    path('mycloset/accessories/<int:accessory_id>/add_accessory_photo/', views.add_accessory_photo, name='add_accessory_photo'),
]