from bs4 import BeautifulSoup
import requests
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}
linkcompleto = "https://www.argentina.gob.ar/coronavirus/informe-diario"
home = "https://www.argentina.gob.ar"

def leerhtmltxt(option):
        L = requests.get(option,headers = headers).text
        return L

# print(leerhtmltxt(linkcompleto))

source = leerhtmltxt(linkcompleto)
def parser(pagina):
    return BeautifulSoup(pagina, "html.parser")

soup = parser(source)
listameses = []
tlincona = soup.find_all("a")

for line in tlincona:
    sacalink = str(line.get( "href"))
    if sacalink.find("informe-diario") != 13:
        continue
    if len(sacalink) < 30:
        continue
    
    linkmensual = home + sacalink
    if linkmensual not in listameses: listameses.append(linkmensual)

# print(listameses)
almacenarloslinks = []

for item in listameses:
    linkmes = leerhtmltxt(item)
    quino = parser(linkmes)
    quinoa = quino.find_all("a")
    igualar = ['btn', 'btn-primary', 'btn-sm']
    for linea in quinoa:
        if len(str(linea)) < 100:
            continue
        if linea.get("class") != igualar:
            continue 
        linkpdf = str(linea.get( "href"))    
        if linkpdf not in almacenarloslinks: almacenarloslinks.append(linkpdf)
    # print(linkpdf)

# print(len(almacenarloslinks))


for item in almacenarloslinks:
    chequear = []
    txtlectura = open("/home/nico/Descargas/Covid/altadescarga.txt","r") 
    for lineatxt in txtlectura:
        chequear.append(lineatxt)
    stringcheck = item + "\n"
    if stringcheck not in chequear:
        archivo = open( "/home/nico/Descargas/Covid/altadescarga.txt", "a")
        archivo.write(stringcheck)
        archivo.close()
    txtlectura.close()

print(len(almacenarloslinks))
print(len(chequear))
# print(chequear)