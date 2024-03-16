import pandas as pd

# creamos una variable donde incluímos la ruta del archivo a analizar
data_file_path = 'pmsm_temperature_data.csv'

# cargamos los datos a un DataFrame de Pandas
df = pd.read_csv(data_file_path)

# Si fuera in archivo excel
# df = pd.read_excel(data_file_path)

# Exploramos los datos
print('print(df.head(n) nos mostrará las primeras 13 filas del dataframe:')
print(df.head(13))
