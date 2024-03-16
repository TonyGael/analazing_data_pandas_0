import pandas as pd

# creamos una variable donde incluímos la ruta del archivo a analizar
data_file_path = 'pmsm_temperature_data.csv'

# cargamos los datos a un DataFrame de Pandas
df = pd.read_csv(data_file_path)

# Si fuera in archivo excel
# df = pd.read_excel(data_file_path)

# Exploramos los datos
print('------------------------------------------------------------------')
print('__________________________________________________________________')
print('print(df.head(n) nos mostrará las primeras 13 filas del dataframe:')
print(df.head(13))

print('------------------------------------------------------------------')
print('__________________________________________________________________')
print('print(df.tal(n) nos mostrará las últimas 13 filas del dataframe:')
print(df.tail(13))

print('------------------------------------------------------------------')
print('__________________________________________________________________')
print('df.shape nos devuelve una tupla con el número de filas y columnas del dataframe:')
print(df.shape)
print('el dataframe tiene {} filas y {} columnas.'.format(df.shape[0], df.shape[1]))

print('------------------------------------------------------------------')
print('__________________________________________________________________')
print('df.columns nos devuelve una lista con los nombres de las columnas del dataframe:')
print(df.columns)

print('------------------------------------------------------------------')
print('__________________________________________________________________')
print('Algunos ,metodos estadísticos con pandas:')
print('df.describe() nos proporciona estadísticas descriptivas para cada columna numérica, '
      'como la mediana, el mínimo, el máximo, los cuartiles:')
print(df.describe())

print('------------------------------------------------------------------')
print('__________________________________________________________________')
print('df.info() nos muestra información sobre el DataFrame, incluyendo el tipo '
      'de datos de cada columna y la cantidad de valores no nulos.')
print(df.info())

# Selección de datos