from django.shortcuts import render
import requests
# Create your views here.


def home(request):
    city = request.POST.get('city', 'comilla')
    apikey = "bd81fb4817e2ad00633fe4292971ec70"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&units=metric"
    data = requests.get(url).json()
    payload = {
        'city': data['name'],
        'weather': data['weather'][0]['main'],
        'icon': data['weather'][0]['icon'],
        'description': data['weather'][0]['description'],
        'temp': int(data['main']['temp']),
        'feels_like': data['main']['feels_like'],
        'temp_min': data['main']['temp_min'],
        'temp_max': data['main']['temp_max'],
        'pressure': data['main']['pressure'],
        'humidity': data['main']['humidity'],
        'visibility': int(data['visibility'] / 1000),
        'country': data['sys']['country']
    }
    context = {'data': payload}

    return render(request, 'home/index.html', context)
