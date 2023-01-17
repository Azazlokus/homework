import requests
from geocode_key import api_key

response = requests.get(f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Москва,+Петровка,+38&format=json")
json_response = response.json()
toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
toponym_postal_code = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["postal_code"]
print(toponym_address + " имеет почтовый индекс " + toponym_postal_code)