from django.shortcuts import render
import json
import urllib.request

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen(
            'https://api.openweathermap.org/data/2.5/weather?q='
            + city + '&appid=0c9f7df03d2ccaffd2ccc14f08d2a39f&lang=ru&units=metric').read()
        
        list_of_data = json.loads(source)

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + 'k',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
        }
        print(data)
    else:
        data = {}
    return render(request, "index.html", data)