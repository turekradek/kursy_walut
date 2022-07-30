import pandas as pd
import matplotlib.pyplot as plt
from random import randint
import a1

url = 'https://www.nbp.pl/kursy/Archiwum/archiwum_tab_a_2022.csv'
kursy = pd.read_csv(url, sep=';',encoding='cp1250',index_col='data')
kursy2 = kursy[1:-3]

def daty(plik):
    url = 'https://www.nbp.pl/kursy/Archiwum/archiwum_tab_a_2022.csv'
    kursy = pd.read_csv(plik, sep=';', encoding='cp1250', index_col='data')
    daty = kursy.index.tolist()
    daty.pop(0)
    daty = [ f'{data[-2:]}-{data[4:6]}-{data[:4]}' for data in daty]
    daty=daty[:-3]
    return daty

def waluty_naglowki(plik):
    waluty = pd.read_csv(plik,sep=';',encoding='cp1250')
    waluty_nag =  waluty.columns.tolist()
    waluty_nag.pop(0)
    waluty_nag = waluty_nag[:-3]
    return waluty_nag

def waluty_wybierz_wiersz(plik,wiersz='20220104'):
    kursy = pd.read_csv(plik, sep=';', encoding='cp1250',index_col='data')
    return kursy.loc[wiersz].to_frame().to_html()



def waluta_wartosc(plik,wiersz='20220103',waluta='1USD'):
    kursy = pd.read_csv(plik, sep=';', encoding='cp1250',index_col='data')
    # print( kursy.loc[wiersz][waluta]  )
    # df.fillna('', inplace=True)
    kursy.fillna('waluta nie notowana',inplace=True)
    # print(kursy.loc[wiersz][waluta])
    # if kursy.loc[wiersz][waluta] == 'NaN':
    #     print( ' nie notowany kurs ')
    return  kursy.loc[wiersz][waluta]



def wykres():
    dane_pocz = a1.zmia
    dane_koniec = kursy2[[]]
    wykres = plt.plot( dane_pocz, dane_koniec )
    plt.savefig('wykres.png')
    plt.show()
    
def daty_zalezne(plik, wartosc='03-01-2022'):
    url = 'https://www.nbp.pl/kursy/Archiwum/archiwum_tab_a_2022.csv'
    kursy = pd.read_csv(plik, sep=';', encoding='cp1250', index_col='data')
    daty = kursy.index.tolist()
    daty.pop(0)
    daty = [f'{data[-2:]}-{data[4:6]}-{data[:4]}' for data in daty]
    daty = daty[:-3]
    gdzie = daty.index(wartosc)
    lista = daty[gdzie:]
    return lista

def slownik_1():
    sl = { chr(65+i): [ str(randint(100,200))  for j in range( 5 ) ]   for i in range( 10 )}
    return sl

print( kursy2.loc[['20220103','20220104']]['1EUR'] )