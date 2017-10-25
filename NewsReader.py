import bs4, requests

linkg1 = 'http://g1.globo.com/'
linkr7 = 'https://noticias.r7.com/'

print('Carregando...')

pegar = requests.get(linkg1)
pegarr7 = requests.get(linkr7)
print('Testando Conexão...')
pegar.raise_for_status()
pegarr7.raise_for_status()
print('Conexão Concluida!\n')
soupg1 = bs4.BeautifulSoup(pegar.text, 'html5lib')
soupr7 = bs4.BeautifulSoup(pegarr7.text, 'html5lib')
sel = soupg1.select('.feed-post-body-title')
selr7 = soupr7.select('.single-trend-news-bullet')
qt = min(3, len(sel))
parr7 = len(selr7)
qtr7 = min(3, parr7)

print('Noticias do G1')
print('Mostrando 3 noticias de {}.'.format(len(sel)))
for i in range(qt):
    print('-' + sel[i].getText())
    

print('\nNoticias do R7')
print('Mostrando 3 noticias de {}.'.format(parr7))
for i in range(qtr7):
    print('-' + selr7[i].getText())
print('FIM')

