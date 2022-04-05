from random import randint
import pandas as pd
import matplotlib.pyplot as plt
def wyrazy():
    lista = []
    for i in range( randint( 5,10)):
        tekst = [ chr(randint(65,90))  for i in range( randint(3,10)) ]
        tekst = ''.join( tekst)
        lista.append( tekst )
    return lista

def liczby():
    lista = [ randint(100 , 500) for i in range( randint(5,10))]
    return lista

def pokemony_nazwy(plik):
    pok = pd.read_csv(plik,sep=',',encoding='utf-8')
    return pok['Name'].tolist()

def pokemony_naglowki(plik):
    pok = pd.read_csv(plik,sep=',',encoding='utf-8')
    return pok.columns.tolist()

def pokemony_wybierz_kolumna(plik,kolumna):
    pok = pd.read_csv(plik, sep=',', encoding='utf-8')
    return pok[kolumna]

def pokemony_wybierz_wiersz(plik,wiersz='Charmander'):
    pok = pd.read_csv(plik, sep=',', encoding='utf-8')
    numer = pok[pok['Name']==wiersz].index
    return pok.iloc[numer].to_html()

def pokemony_wybierz_wartosc(plik,kolumna, wiersz='Charmander'):
    pok = pd.read_csv(plik, sep=',', encoding='utf-8')
    numer = pok[pok['Name'] == wiersz].index
    return str(pok.iloc[numer][kolumna]).split()[1]

def wykres():
    dane = [1,2,3,4,5,6,7,8,9]
    dane2 = [10,20,23,30,40,40,45,39,70]
    wykres = plt.plot( dane, dane2 )
    plt.savefig('wykres.png')
    plt.show()



# plik = 'pokemon.csv'
# a = pokemony_wybierz_wartosc(plik, 'HP', 'Bulbasaur')
# print( a )
# print(  a.split() )from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
# from matplotlib.figure import Figurefrom matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
# from matplotlib.figure import Figure
