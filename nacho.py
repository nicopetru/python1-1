import requests
import re
from bs4 import BeautifulSoup
# from tqdm import tqdm
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}
urlFrom = "https://www.argentina.gob.ar/coronavirus/informe-diario/junio2020"
regexpCoarse = re.compile(r'(\.pdf)+')

# Connect to the URL
response = requests.get(urlFrom, headers = headers)
# Parse HTML and save to BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")

for one_a_tag in soup.findAll('a', attrs={'href' : regexpCoarse}):
    link = one_a_tag['href']
    print(link)
    r = requests.get(link, stream = True)   #,stream=True
    print(r.headers['content-type'])
    print("")