# -*- coding: utf-8 -*-
"""clase_15

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/125HsYv4Ud9KjJoietLmklMEovZnNQwzj
"""

import streamlit as st
import pandas as pd

# Título de la aplicación
st.title('Aplicación de Análisis de Datos')

# Cargar el archivo CSV
uploaded_file = st.file_uploader('Sube tu archivo CSV', type=['/content/database_titanic.csv'])

if uploaded_file is not None:
   # Leer el archivo CSV usando Pandas
   #This line was not indented correctly and caused the error.
   df = pd.read_csv(uploaded_file)
   # Mostrar las primeras filas del archivo
   st.write('Primeras 5 filas del archivo:')
   st.write(df.head())