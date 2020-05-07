
from bs4 import BeautifulSoup
import requests
import re
from random import randint

rdm = randint(1,400)

print("Bajamos el libro #: " + rdm)
# https://docs.google.com/spreadsheets/d/1HzdumNltTj2SHmCv3SRdoub8SvpIEn75fa4Q23x0keU/htmlview?fbclid=IwAR10EFL8JMRtaqfbx8f3ccEFu5hs-XGxChRNcYxs1N3Z_ztAG2F3eEblkvw
link = "https://docs.google.com/spreadsheets/d/1HzdumNltTj2SHmCv3SRdoub8SvpIEn75fa4Q23x0keU/htmlview?fbclid=IwAR10EFL8JMRtaqfbx8f3ccEFu5hs-XGxChRNcYxs1N3Z_ztAG2F3eEblkvw"
# link de mati donde esta la lista de libros

def leerhtmltxt(option):
        L = requests.get(option).text
        return L


source = leerhtmltxt(link)

#el & lo lee como &amp asi que hay q borrar las entradas erroneas
source = re.sub(r"&amp;","&",source)

# necesito copiar esto \ ^ porq no se escribirlo con el teclado
x = re.findall(r"(http://lin+[\w\./?&=;-]+)",str(source))

paradescarga = leerhtmltxt(x[rdm])

#hay que buscar el home porq en el link de descarga le falta
home = re.findall(r"(http?://\S+)/",x[rdm])

#intentando hacer andar BS4
soup = BeautifulSoup(paradescarga, "html.parser")

#sacamos el titulo del libro para el archivo PDF
tit = soup.title.string
tit = tit[0:tit.index("|")-1]

tlincona = soup.find_all("a")

#hay que crear una lista para agregar links de descarga:
ldown = [] 

#pasamos las lineas para sacar el link de descarga
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

print("Se va a crear: "+"/home/nico/Descargas/Mati-PDF/" + tit + ".pdf")



lfinal = requests.get(ldown[0])
open("/home/nico/Descargas/Mati-PDF/" + tit + ".pdf" , "wb").write(lfinal.content)