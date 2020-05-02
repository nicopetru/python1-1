from bs4 import BeautifulSoup
import requests
import re

link = "http://link.springer.com/openurl?genre=book&isbn=978-3-319-26551-3"
html = requests.get(link).text

soup = BeautifulSoup(html, "html.parser")
lincona = soup.a


print(type(soup))
print(soup.title)
print(lincona)
print(lincona.text)
print(lincona.get("href"))
print("hay que buscar la linea de donwload")

