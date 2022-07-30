import pandas as pd
url = 'https://www.nbp.pl/kursy/Archiwum/archiwum_tab_a_2022.csv'
kursy = pd.read_csv( url , sep=';', encoding='cp1250')
euro = kursy['1EUR']
print( euro )
