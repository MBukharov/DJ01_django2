from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('city/<str:city>',views.city, name='city'),
]