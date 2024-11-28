from django.shortcuts import render
from .models import News
# Create your views here.

def index_news(request):
    news = News.objects.all()
    data = {
        'news': news
    }
    return render(request, 'news/index_news.html', data)