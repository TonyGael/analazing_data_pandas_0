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
print('------------------------------------------------------------------')
print('__________________________________________________________________')
print('Se puede seleccionar columnas específicas '
      'utilizando la notación de corchetes o el método: '
      'df[["column_x"], ["column_y"]]')
print(df[['motor_speed', 'torque']])

# Agrupación y resumen
print('------------------------------------------------------------------')
print('__________________________________________________________________')
print('df.groupby("columna_x").mean() agrupa los datos por los valores '
      'únicos de una columna y calcula la media para cada grupo')
# print(df.groupby('torque').median()) #  CORREGIR ERROR DE PRESENTACION

print('------------------------------------------------------------------')
print('__________________________________________________________________')
print('POdemos filtrar filas utilizando operaciones lógicas:'
      'df[df[columna_x] > valor]')
print(df[df['motor_speed'] < 0])

# Manejo de valores nulos
print('------------------------------------------------------------------')
print('__________________________________________________________________')
print('df.isnull() nos devuelve un datafeame booleano indicando que valores son nulos')
print(df.isnull())

print('------------------------------------------------------------------')
print('__________________________________________________________________')
print('df.dropna() elimina las filas con estos valores nulos')
print(df.dropna())

print('------------------------------------------------------------------')
print('__________________________________________________________________')
print('df.fillna("valor") rellena los valores nulos con un valor específico')
print(df.fillna('COMPLETAR'))
