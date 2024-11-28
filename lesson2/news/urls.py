from django.urls import path, include
from . import views
from .models import News

urlpatterns = [
    path('', views.index_news, name='show_news'),
]