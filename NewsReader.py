'''
[Pt-Br]Pega notícias dos jornais
[Eng]Get news from newsspapers 
'''

import bs4, requests, time
from datetime import date

print('Iniciando o código...')
#Links 
linkg1 = 'http://g1.globo.com/'
linkr7 = 'https://noticias.r7.com/'
linkTG = 'https://www.theguardian.com/international'

#Get each link with requests
print('Carregando...')
pegar = requests.get(linkg1)
pegarr7 = requests.get(linkr7)
pegarTG = requests.get(linkTG)

print('Testando Conexão...')
pegar.raise_for_status()
pegarr7.raise_for_status()
print('Conexão Concluida!\n')

#Using bs4 and tml5lib to parse
soupg1 = bs4.BeautifulSoup(pegar.text, 'html5lib')
soupr7 = bs4.BeautifulSoup(pegarr7.text, 'html5lib')
soupTG = bs4.BeautifulSoup(pegarTG.text, 'html5lib')

#Getting the text of news
sel = soupg1.select('.feed-post-body-title')
selr7 = soupr7.select('.single-trend-news-bullet')
selTG = soupTG.select('.u-faux-block-link__overlay')

#The min amount(in this case, 4) to print in the loop 
qt = min(4, len(sel))
qtr7 = min(4, len(selr7))
qtTG = min(4, len(selTG))


print('Noticias do G1')
print('Mostrando 3 noticias de {}.'.format(len(sel)))
for i in range(qt):      #Loop for print each line
    print('-' + sel[i].getText())
    

print('\nNoticias do R7')
print('Mostrando 3 noticias de {}.'.format(len(selr7)))
for i in range(qtr7):
    print('-' + selr7[i].getText())


print('Noticias do The Guardian.')
print('Mostrando 3 noticias de {}.'.format(len(selTG)))
for i in range(qtTG):
    print('-' + selTG[i].getText())

#Print Date and Hour
Tatual = time.strftime('%H:%M:%S')
Datual = date.today()
print('\nNotícias atualizadas em:\n{}\n{}'.format(Datual, Tatual))

print('\nFIM')

