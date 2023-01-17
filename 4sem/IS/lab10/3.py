import requests
from geocode_key import api_key

response = requests.get(f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Москва,+Красная+площадь,+1&format=json")
json_response = response.json()
toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
toponym_coodrinates = toponym["Point"]["pos"]
print(toponym_address, "имеет координаты:", toponym_coodrinates)
