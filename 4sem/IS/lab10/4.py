import requests
from geocode_key import api_key

response = requests.get(f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Барнаул&format=json")
json_response = response.json()
toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
toponym_region = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][2]["name"]
print("Барнаул: " + toponym_region)

response = requests.get(f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Мелеуз&format=json")
json_response = response.json()
toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
toponym_region = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][2]["name"]
print("Мелеуз: " + toponym_region)

response = requests.get(f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Йошкар-Ола&format=json")
json_response = response.json()
toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
toponym_region = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][2]["name"]
print("Йошкар-Ола: " + toponym_region)

