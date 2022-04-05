import pandas as pd
import matplotlib.pyplot as plt

url = 'https://www.nbp.pl/kursy/Archiwum/archiwum_tab_a_2022.csv'
kursy = pd.read_csv(url, sep=';', encoding='cp1250', index_col='data')


# print( kursy)
def daty(plik):
    url = 'https://www.nbp.pl/kursy/Archiwum/archiwum_tab_a_2022.csv'
    kursy = pd.read_csv(plik, sep=';', encoding='cp1250', index_col='data')
    daty = kursy.index.tolist()
    daty.pop(0)
    daty = [f'{data[-2:]}-{data[4:6]}-{data[:4]}' for data in daty]
    daty = daty[:-3]
    return daty


def waluty_naglowki(plik):
    waluty = pd.read_csv(plik, sep=';', encoding='cp1250')
    waluty_nag = waluty.columns.tolist()
    waluty_nag.pop(0)
    waluty_nag = waluty_nag[:-3]
    return waluty_nag


def waluty_wybierz_wiersz(plik):
    kursy = pd.read_csv(plik, sep=';', encoding='cp1250',index_col='data')
    return kursy['20220104']


print(waluty_wybierz_wiersz(url))


def wykres():
    dane = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    dane2 = [10, 20, 23, 30, 40, 40, 45, 39, 70]
    wykres = plt.plot(dane, dane2)
    plt.savefig('wykres.png')
    plt.show()


print(waluty_naglowki('https://www.nbp.pl/kursy/Archiwum/archiwum_tab_a_2022.csv'))

