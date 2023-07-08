import requests
from datetime import datetime

from django.shortcuts import render


# Create your views here.
def index(request):
    try:
        if request.method == 'POST':
            API_KEY = ''
            city_name = request.POST.get('city')
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'
            response = requests.get(url).json()
            current_time = datetime.now()
            formatted_time = current_time.strftime("%A, %B %d %Y, %H:%M:%S %p")
            city_weather = dict(
                city=city_name.capitalize(),
                description='Description: {description}'.format(description=response['weather'][0]['description']),
                icon=response['weather'][0]['icon'],
                temperature='Temperature: {temperature} °C'.format(temperature=response['main']['temp']),
                country_code=response['sys']['country'],
                wind='Wind: {wind_speed} km/h'.format(wind_speed=response['wind']['speed']),
                humidity='Humidity: {humidity} %'.format(humidity=response['main']['humidity']),
                time=formatted_time
            )
        else:
            city_weather = dict()

        context = {'city_weather': city_weather}
        return render(request, 'weather/home.html', context)
    except:
        return render(request, 'weather/404.html')
