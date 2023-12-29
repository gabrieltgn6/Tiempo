import requests
import openpyxl
from pprint import pprint
import os

API_Key = "6f87c7db27d128776085cc14992324ef"

city = input("¿Qué ciudad quieres consultar? ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

weather_data = requests.get(base_url).json()

# Imprimir los datos obtenidos
pprint(weather_data)

# Nombre del archivo Excel
excel_file = f'{city}_weather_data.xlsx'

# Si el archivo ya existe, cargar el libro de trabajo existente
if os.path.exists(excel_file):
    workbook = openpyxl.load_workbook(excel_file)
    sheet = workbook.active
else:
    # Si el archivo no existe, crear uno nuevo
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    # Escribir encabezados si es un nuevo archivo
    sheet.append(["Key", "Value"])

# Escribir los datos en el archivo Excel
for key, value in weather_data.items():
    # Convertir las listas y diccionarios a cadenas antes de escribirlos en Excel
    if isinstance(value, (list, dict)):
        value = str(value)
    sheet.append([key, value])

# Guardar el archivo Excel
workbook.save(excel_file)

print(f"Datos agregados a {excel_file}")
