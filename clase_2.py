import pandas as pd
import openpyxl

'''IMPORTAR DATOS DESDE UN ARCHIVO'''
df = pd.read_csv('pokemon_data.csv')
pd.set_option("display.max_columns",None)

'''FILTRADO DE DATOS'''
#print(df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP']>70)]) #& |
#nuevo_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP']>70)]
#nuevo_df = nuevo_df.reset_index(drop=True)
#print(nuevo_df)
#nuevo_df.to_csv('pokemons_planta_veneno_70.csv')
#print(df.head(25))

#~ ALT + 126

#print(df.loc[df['Name'].str.contains('Mega')])
#print(df.loc[~df['Name'].str.contains('Mega')])

import re
#print(df.loc[df['Name'].str.contains('^Ve[a*z]*',flags = re.I,regex = True)]) #^Empieza por,,, *1 o más letras entre la a y la z

'''CAMBIOS CONDICIONALES'''
#print(df.head(10))
#df.loc[df['Type 1'] == 'Grass','Type 1'] = 'Planta'
#df.loc[df['Type 1'] == 'Fire','Legendary'] = True
#print(df.head(10))

#df.loc[df['Speed']> 70,['Generation','Legendary']] = 'Rapido', True
#print(df.head(10))

'''SACAR ESTADÍSTICAS'''
print(df.groupby(['Type 1']).mean(numeric_only=True).sort_values('Attack',ascending=False))
#print(df.groupby(['Type 1']).count())
df['Count'] = '1'
print(df.groupby(['Type 1']).count()['Count'])

