import requests

listadelibros = "https://docs.google.com/spreadsheets/d/1HzdumNltTj2SHmCv3SRdoub8SvpIEn75fa4Q23x0keU/htmlview?fbclid=IwAR10EFL8JMRtaqfbx8f3ccEFu5hs-XGxChRNcYxs1N3Z_ztAG2F3eEblkvw"

paginadeunodeloslibros = "http://link.springer.com/openurl?genre=book&isbn=978-3-319-26551-3"

paginadedescargadellibro = "https://link.springer.com/content/pdf/10.1007%2F978-3-319-26551-3.pdf"

paglist = [listadelibros , paginadeunodeloslibros, paginadedescargadellibro]

numarchivo = 0

def extraer(pag):
    link = requests.get(pag).text
    archivo.write(link)


for x in paglist:
#    print("Desafio-" +str(nombredelarchivo)+".txt")
#    el print era para probar como escribir el nombre del archivo
    nombre = "Desafio-" + str(numarchivo) + ".txt"
    archivo = open( nombre , "w")
    extraer(x)
    numarchivo += 1 
    archivo.close()

print("a ver github")