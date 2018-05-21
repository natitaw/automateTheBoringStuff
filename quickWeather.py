#! python3
# quickWeather.py   - pulls weather data (for today and next two days)
# from OpenWeatherMap.org and prints it to screen


import json, requests, sys

# Get location from cmd

countryCode = 'NL'

if len(sys.argv) < 2:
    print('Usage: quickweather.py <location>')
    sys.exit()

location = ' '.join(sys.argv[1:])

# TODO: Download the JSON data from OpenWeatherMap.org's API

url ='http://openweathermap.org/data/2.5/forecast?q=%s,%2s&appid=b6907d289e10d714a6e88b30761fae22' % (location, countryCode)

response = requests.get(url)
response.raise_for_status()

weatherData = json.loads(response.text)

# Print weather descriptions

w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
