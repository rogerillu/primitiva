import urllib2
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

pagina_buscar ='http://www.loteriasyapuestas.es/es/la-primitiva'
page = urllib2.urlopen(pagina_buscar)
soup = BeautifulSoup(page, 'html.parser')

#name_box = soup.find_all('ul')
name_box = soup.find('div',attrs={'class': 'cuerpoRegionIzq'})

date = soup.find('a',attrs={'id': 'lastResultsTitleLink'})

boles = soup.find_all('span','bolaPeq')

date_today = date.text.split()
bola_comp = boles[0].text.split()
bola_rein = boles[1].text.split()

lista = name_box.text.split()
nom = "{} {}:\n".format(lista[0],lista[1])
numeros = lista[2:7]
text_num = " ".join(numeros)

print("\n{}: {}".format(date_today[0],date_today[1][0:2]))
print("\nFecha: {}\n".format(date_today[2]))
print(nom)
print(text_num)
print("\nComplementario: {}".format(bola_comp[0]))
print("\nReintegro {}".format(bola_rein[0]))

print("\n   ")
