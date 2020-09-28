import requests

googledoc = "https://docs.google.com/forms/d/e/1FAIpQLScmKCVxotFPtqiRSXCD-P0L7DLUR7_ok85Eph7XatRvD5DCdQ/viewanalytics"

archivo = open( "alto-leak3.txt" , "w")

link = requests.get(googledoc).text
archivo.write(link)
print("termine")