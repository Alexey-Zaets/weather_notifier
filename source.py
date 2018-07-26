from os.path import abspath

key = ''  # API key
city = ''  # city name
path = abspath('icons')

icons = {
        'clear sky': '--icon={}/weather-clear.svg'.format(path),
        'few clouds': '--icon={}/weather-few-clouds.svg'.format(path),
        'scattered clouds': '--icon={}/weather-clouds.svg'.format(path),
        'broken clouds': '--icon={}/weather-overcast.svg'.format(path),
        'shower rain': '--icon={}/weather-shower-scattered.svg'.format(path),
        'rain': '--icon={}/weather-shower.svg'.format(path),
        'thunderstorm': '--icon={}/weather-storm.svg'.format(path),
        'snow': '--icon={}/weather-snow.svg'.fomat(path),
        'mist': '--icon={}/weather-fog.svg'.format(path),
        }
