import requests
from geocode_key import api_key

# A
request = requests.get(f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Якутск&format=json")
request = requests.get(f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Магадан&format=json")

# B
request = requests.get(f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Белово&format=json")
request = requests.get(f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Торонто&format=json")

# C
request = requests.get(f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Хабаровск&format=json")
request = requests.get(f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Уфа&format=json")
request = requests.get(f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Нижний+Новгород&format=json")
request = requests.get(f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Калининград&format=json")
request = requests.get(f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Белово&format=json")

# D
request = requests.get(f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Кемерово,+ул.+Красная+6&format=json")

