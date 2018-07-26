"""This is a weather notifier for UNIX-like OS."""

from time import sleep
from subprocess import call
from requests import get
from source import key, city, icons

def weather_message():
    """This function creates and sends messages of the  current weather forecast to the desktop."""
    api_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'units': 'metric',
        'appid': key,
        }
    request = get(api_url, params=params)
    data = request.json()
    try:
        image = icons[data['weather'][0]['description']]
        data = data['main']
        title = 'Current weather in {}:'.format(city)
        template = 'Temperature: {} C\nHumidity: {} %\nAtmospheric pressure: {} hPa\n'
        message = template.format(round(data['temp']), data['humidity'], data['pressure'])
    except KeyError:
        call(['notify-send', 'Error'])
    call(['notify-send', image, title, message])
    sleep(3600.0)
    weather_message()

weather_message()
