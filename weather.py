import requests
import openpyxl
from pprint import pprint

API_Key = "6f87c7db27d128776085cc14992324ef"

city = input("¿Qué ciudad quieres consultar? ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

weather_data = requests.get(base_url).json()

# Imprimir los datos obtenidos
pprint(weather_data)

# Crear un archivo Excel y escribir los datos
workbook = openpyxl.Workbook()
sheet = workbook.active

# Escribir los datos en el archivo Excel
for key, value in weather_data.items():
    # Convertir las listas y diccionarios a cadenas antes de escribirlos en Excel
    if isinstance(value, (list, dict)):
        value = str(value)
    sheet.append([key, value])

# Guardar el archivo Excel
workbook.save(f'{city}_weather_data.xlsx')

print(f"Datos guardados en {city}_weather_data.xlsx")
