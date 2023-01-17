from bs4 import BeautifulSoup
import requests
from random import choice

url = "https://quotes.toscrape.com/"
page = "page/"
count_page = 10
quotes = []

for i in range(count_page):
    response = requests.get(url+page+str(i+1))
    soup = BeautifulSoup(response.text, "html.parser")
    for quote in soup.find_all("span", class_="text"):
        quotes.append(quote.text)

for i in range(5):
    print(i+1, ")", sep="")
    print(choice(quotes))
    
