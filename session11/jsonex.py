import json
import urllib.request

def get_temp(cityname, countrycode):
    APIKEY = '9a0b0d2f3c90bbee4b839bcc2e968205'
    city = cityname
    country = countrycode
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&APPID={APIKEY}'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    temp = int(response_data['main']['temp'])
    return (f"The Temperature in {city} is {temp}")

print(get_temp("Yangon", "mm"))