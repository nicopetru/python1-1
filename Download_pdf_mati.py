
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

print(type(source))
source = re.sub(r"&amp;","&",source)
# necesito copiar esto \ ^
x = re.findall(r"(http://lin+[\w\./?&=;-]+)",str(source))

# link q anda   http://link.springer.com/openurl?genre=book&isbn=978-3-319-26551-3
#link q no anda http://link.springer.com/openurl?genre=book&amp;isbn=978-3-319-26551-3
print(x[390])
print("findall encontro ", len(x), "links para descargar")
paradescarga = leerhtmltxt(x[390])
pd = paradescarga.split()

#intentando hacer andar BS4
soup = BeautifulSoup(paradescarga, "html.parser")
lincona = soup.a
print("Link BS4")
print(lincona) 

print("Sin BS4")
for line in pd:
        if len(line) < 30:continue
        if re.search("content/pdf",line):
                print(line)
#for line in source:
#    if len(line) < 25: continue
#    countlineas += 1
#    if re.findall("http",line):
#        print(line)
#        countlinks += 1
#    if re.search(r"http",line):
#        print(line)
#        count = count + 1 

# fin de la pag </div>
#print("Econtramos " , countlinks , "lineas.")