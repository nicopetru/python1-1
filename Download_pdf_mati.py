
from bs4 import BeautifulSoup

import requests
import re
from random import randint
countlineas = 0
countlinks = 0
rdm = randint(1,400)
print(rdm)
# https://docs.google.com/spreadsheets/d/1HzdumNltTj2SHmCv3SRdoub8SvpIEn75fa4Q23x0keU/htmlview?fbclid=IwAR10EFL8JMRtaqfbx8f3ccEFu5hs-XGxChRNcYxs1N3Z_ztAG2F3eEblkvw
link = "https://docs.google.com/spreadsheets/d/1HzdumNltTj2SHmCv3SRdoub8SvpIEn75fa4Q23x0keU/htmlview?fbclid=IwAR10EFL8JMRtaqfbx8f3ccEFu5hs-XGxChRNcYxs1N3Z_ztAG2F3eEblkvw"
# link de mati donde esta la lista de libros

def leerhtmltxt(option):
        L = requests.get(option).text
        return L

source = leerhtmltxt(link)
#source = source.split()

#print(type(source))
source = re.sub(r"&amp;","&",source)
# necesito copiar esto \ ^
x = re.findall(r"(http://lin+[\w\./?&=;-]+)",str(source))

# link q anda   http://link.springer.com/openurl?genre=book&isbn=978-3-319-26551-3
#link q no anda http://link.springer.com/openurl?genre=book&amp;isbn=978-3-319-26551-3
#print(x[390])
#print("findall encontro ", len(x), "links para descargar")
paradescarga = leerhtmltxt(x[rdm])
#hay que buscar el home porq en el link de descarga le falta
home = re.findall(r"(http?://\S+)/",x[rdm])
pd = paradescarga.split()
#print(x[3])
#intentando hacer andar BS4
soup = BeautifulSoup(paradescarga, "html.parser")
tlincona = soup.find_all("a")

#hay que crear una lista para agregar links de descarga:
ldown = [] 
#print(type(ldown))
#print("Link BS4")
for line in tlincona:     
        #esto devuelve todos los title
        #print(line.get( "title"))
        #vamos a filtrarlos
        if line.get("title") == None: continue
        if line.get("title") != "Download this book in PDF format": continue 
        sacalink = str(line.get( "href"))
        sacalink = home[0]+sacalink
        if sacalink not in ldown: ldown.append(sacalink)
#print(ldown)

#hasta aca, ya devuelve el link de descarga sin el home
#y lo agrega a la lista sin duplicar (porq en la pagina
#estan dos veces los links

lfinal = requests.get(ldown[0])
open("/home/nico/Descargas/Mati-PDF/pdf1.pdf" , "wb").write(lfinal.content)