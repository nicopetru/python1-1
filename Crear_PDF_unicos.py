import re
import requests
import os

archivo = open("/home/nico/Descargas/Covid/altadescarga.txt","r") 
listadescarga = []

for line in archivo:
    line = line.rstrip('\n')
    listadescarga.append(line)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}
carpetainformes = "/home/nico/Descargas/Covid/informes/"

# url1 = 'https://readthedocs.org/projects/python-guide/downloads/pdf/latest/'
# url ='https://www.argentina.gob.ar/sites/default/files/18-05-20-reporte-matutino-covid-19.pdf'
# myfile = requests.get(url)
# myfile1 = requests.get(url1)
# open(carpetainformes + 'prueba.pdf', 'wb').write(myfile.content)
# open(carpetainformes + 'prueba.pdf1', 'wb').write(myfile1.content)
# print("PDF del gobierno" , myfile.headers['content-type'])
# print("PDF que funciona" , myfile1.headers['content-type'])



for line in listadescarga:
    # print(line)
    nombre = line.strip('https://www.argentina.gob.ar/sites/default/files/') + ".pdf"
    nombrearchivo = carpetainformes[1:] + nombre
    print(nombrearchivo)
    if nombre not in os.listdir(carpetainformes):
        lfinal = requests.get(line, headers = headers)
        open( "/home/nico/Descargas/Covid/informes/" + nombre , "wb").write(lfinal.content)
    else:
        print("ya esta")

print("Termine")