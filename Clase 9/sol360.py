import requests
import pprint
import json

key = 'f6aebc1f999ab9b6a8685e0d60bd5373'

archivo_in = open('sucursales_sol_360.csv')

for linea in archivo_in:
    linea = linea.split(';')
    print(linea[0])
    ciudad_cod = requests.utils.quote(linea[0])
    provincia_cod = requests.utils.quote(linea[1])
    url = 'https://api.openweathermap.org/data/2.5/weather?q=' + ciudad_cod + ',Argentina&lang=es&appid=' + key
    objeto = json.loads(requests.get(url).text)
    descripcion = objeto.get('weather')[0]['description']
    
