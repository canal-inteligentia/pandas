import pandas as pd
import openpyxl

'''IMPORTAR DATOS DESDE UN ARCHIVO'''
df = pd.read_csv('pokemon_data.csv')
pd.set_option("display.max_columns",None)

'''OBSERVAR LOS DATOS'''
#print(df.head(4))
#print(df.tail(4))
#print(df.columns)
#print('\n')
#print(df['Name'][780:])
#print(df[['Name','Type 1','Speed']])
#print(df.iloc[0,5])

'''ITERAR A LO LARGO DE LA BASE DE DATOS
for index,row in df.iterrows():
    if row['Type 1'] == 'Fire':
        print(index,row['Name'])'''

#print(df.describe())

'''ORGANIZAR UNA BASE DE DATOS'''
#print(df.sort_values(['Name','Type 1'],ascending=[1,0]))

'''HACER CÁLCULOS SACAR NUEVAS COLUMNAS'''
#print(df.head(2))
#df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
#print(df['Total'])
df['Total'] = df.iloc[:,4:10].sum(axis=1) #horizontal
#print(df.head(4))
cols = list(df.columns.values)
print(cols)
df = df[cols[0:4]+[cols[-1]]+cols[4:12]]
print(df.head(4))

df.to_excel('nueva_bbdd_poke.xlsx',index=False)