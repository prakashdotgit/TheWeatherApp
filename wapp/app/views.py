from django.shortcuts import render
import requests
import os
# Create your views here.
def index(request):
    city = request.GET.get('city')
    api_key="8f028d5c51044649d8dc34b48eca1ea1"

    # api_key = os.getenv("OPENWEATHER_API_KEY")
    
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    print(api_url)
    api = requests.get(api_url).json()
    temperature=api['main']['temp']

    wind_speed = api['wind']['speed']
    humidity = api['main']['humidity']
    name = api['name']
    country = api['sys']['country']
    icon = api['weather'][0]['icon']
    weather = api["weather"][0]['main']
    description = api['weather'][0]['description']
    img_url = f"https://openweathermap.org/img/wn/{icon}@2x.png"

    city = api['name']
    country = api['sys']['country']
    # return render(request,'index.html',{'temperature':temperature, 'city':city, 'country':country})
    return render(request, 'index.html', {'temperature':temperature, 'city':city, 'wind_speed':wind_speed, 'humidity':humidity, 'name':name,'country':country,'img_url':img_url, 'weather':weather, 'description':description})

