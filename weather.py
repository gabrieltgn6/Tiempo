import requests
from pprint import pprint

API_Key = "6f87c7db27d128776085cc14992324ef"

city = "Tarragona"

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data) 
