from bs4 import BeautifulSoup
import requests

url = "http://olympus.realpython.org"
response = requests.get(url + "/profiles")
soup = BeautifulSoup(response.text, "html.parser")

for link in soup.find_all("a"):
    print(url + link.get("href"))
