import requests

response = requests.get("https://static-maps.yandex.ru/1.x/?ll=86.098886%2C55.355069&spn=0.07,0.07&l=map&" +
                        "pt=86.060110%2C55.344206,pm2dgm1~86.125956%2C55.388892,pm2lbm2~86.071900%2C55.375493," + 
                        "pm2ywm3~86.128400%2C55.342512,pm2dom4")
map_file = "map_kemerovo_marks.png"
with open(map_file, "wb") as file:
    file.write(response.content)