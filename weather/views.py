import requests
from django.shortcuts import render

def index(request):
    appid = '9549f93f8304db2f6cd0cd9a4fd458e0'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    city = 'London'
    res = requests.get(url.format(city)).json()

    city_info ={
        'city':city,
        'temp': res["main"]["temp"],
        'icon': res["weather"][0]["icon"]
    }

    context = {'info': city_info}

    return render(request, 'weather/index.html', context)

def about(request):
    return render(request, 'weather/about.html')
