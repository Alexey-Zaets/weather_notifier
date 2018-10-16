#!/usr/bin/python3
"""
This is a weather notifier for UNIX-like OS.
"""

from source import icons 
import time, subprocess, requests, json

def weather_message(record):
    """This function creates and sends messages of the  current weather forecast to the desktop."""
    api_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
            'q': record['CITY'], 
            'units': record['UNITS'], 
            'appid': record['APPID']
            }
    request = requests.get(api_url, params=params)
    data = request.json()
    try:
        image = icons[data['weather'][0]['description']]
        data = data['main']
        title = 'Current weather in {}:'.format(record['CITY'])
        template = 'Temperature: {} C\nHumidity: {} %\nAtmospheric pressure: {} hPa\n'
        message = template.format(round(data['temp']), data['humidity'], data['pressure'])
    except KeyError:
        subprocess.call(['notify-send', 'Error with icons path'])
    subprocess.call(['notify-send', image, title, message])
    time.sleep(3600)
    weather_message(record)

def start():
    try:
        with open('settings.json') as f:
            data = f.readline().rstrip()
        record = json.loads(data)
        weather_message(record)
    except FileNotFoundError:
        city = input('Enter your city: ').capitalize()
        while city == '':
            city = input('Enter your city: ').capitalize()
        appid = input('Enter your appid key: ')
        while appid == '':
            appid = input('Enter your appid key: ')
        units = input(
            'Enter units "imperial" for temperature in Fahrenheit \
or "metric" for temperature in Celsius. \
Temperature in Kelvin is used by default: '
            )
        data = {
            'CITY' : city,
            'APPID' : appid,
            'UNITS' : units,
            }
        with open('settings.json', 'w') as f:
            f.write(json.dumps(data))
        start()

if __name__ == '__main__':
    start()
