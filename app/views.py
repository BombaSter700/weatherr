from django.shortcuts import render, redirect
import json
import urllib.request

history = []

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen(
            'https://api.openweathermap.org/data/2.5/weather?q='
            + city + '&appid=СЮДА_СВОЙ_API&lang=ru&units=metric').read()
        
        list_of_data = json.loads(source)

        data = {
            "city": city,
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + '°C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            "description": list_of_data['weather'][0]['description'],
            "datetime": list_of_data['dt']
        }

        history.append(data)
        print(data)
    else:
        data = {}
    return render(request, "index.html", data)

def history_view(request):
    return render(request, "history.html", {"history": history})
