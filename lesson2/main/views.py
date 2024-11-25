from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'main/index.html',)

def city(request,city):
    data = {
        'city': city
    }
    if city == 'Москва':
        return render(request, 'main/Moscow.html', data)
    if city == 'Казань':
        return render(request, 'main/Kazan.html', data)
    if city == 'Екатеринбург':
        return render(request, 'main/Ekb.html', data)
    if city == 'Сочи':
        return render(request, 'main/Sochi.html', data)