from django.shortcuts import render
import requests
import os
# Create your views here.
def index(request):
    city = request.GET.get('city')
    api_key="e65698cb134926642f96a3679e5ff986"
    #api_key = os.getenv("OPENWEATHER_API_KEY")
    
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    print(api_url)
    api = requests.get(api_url).json()
    temperature=api['main']['temp']
    city = api['name']
    country = api['sys']['country']
    wind_speed = api['wind']['speed'] 
    humidity = api['main']['humidity'] 
    icon = api['weather'][0]['icon'] 
    weather = api["weather"][0]['main'] 
    description = api['weather'][0]['description']

    img_url = f"https://openweathermap.org/img/wn/{icon}@2x.png"


    return render(request,'index.html',{'temp':temperature, 
                                        'city':city, 
                                        'country':country, 
                                        'wind_speed':wind_speed, 
                                        'humidity':humidity, 
                                        'country':country,
                                        'img_url':img_url,
                                        'weather':weather, 
                                        'description':description})
