from bs4 import BeautifulSoup
import requests

url = "https://quotes.toscrape.com/"
page = "page/"
count_page = 10
authors = {}

for i in range(count_page):
    response = requests.get(url+page+str(i+1))
    soup = BeautifulSoup(response.text, "html.parser")
    for author in soup.find_all("small", class_="author"):
        if author.text not in authors:
            authors[author.text] = 1
        else:
            authors[author.text] += 1

sorted_tuples = sorted(authors.items(), key=lambda item: -item[1])
sorted_authors = {k: v for k, v in sorted_tuples}

for k, v in sorted_authors.items():
    print(k, ": ", v)