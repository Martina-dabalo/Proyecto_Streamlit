# TODO: Aquí debes escribir tu código

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing()

df_california = pd.DataFrame(housing.data, columns=housing.feature_names)
df_california['MedHouseVal'] = housing.target

st.title("California Housing Data App")
#st.dataframe(df_california.head())

st.sidebar.markdown('## Filtros interactivos')

min_age = df_california['HouseAge'].min()

max_age = df_california['HouseAge'].max()

rango_age = st.sidebar.slider('Edad mediana de la casa: ', min_value=min_age, max_value=max_age, value=(min_age, max_age))

df_filtrado = df_california[(df_california['HouseAge'] >= rango_age[0]) & (df_california['HouseAge'] <= rango_age[1])]

#st.dataframe(df_filtrado.head())

if st.sidebar.checkbox('Filtrar por latitud mínima'):
    lat_min = (df_california['Latitude'].min())
    lat_min_ = st.number_input('Latitud mínima: ', value=lat_min)
    # df_filtrado2 = df_california[df_california['Latitude'] >= lat_min_]
    df_filtrado = df_filtrado[df_filtrado['Latitude'] >= lat_min_]

mediana = df_filtrado['MedHouseVal'].median()
rango = (df_filtrado['MedHouseVal'].max()) - (df_filtrado['MedHouseVal'].min())

st.subheader('Resume descriptivo de la vivienda')
st.write(f'Mediana: {mediana}')
st.write(f'Rango: {rango}')

st.dataframe(df_filtrado.head())

fig, ax = plt.subplots()
ax.hist(df_filtrado['MedHouseVal'], bins=30, color='skyblue', edgecolor='black')
ax.set_title('Distribución del valor mediano de la vivienda')
ax.set_xlabel('MedHouseVal')
ax.set_ylabel('Frecuencia')

st.pyplot(fig)

fig2, ax = plt.subplots()
x = df_filtrado['MedInc']
y = df_filtrado['MedHouseVal']
ax.scatter(x, y, color='purple')

ax.set_title('Relación entre Ingresos y Valor de la Vivienda')
ax.set_xlabel('Mediana de Ingresos (MedInc)')
ax.set_ylabel('Valor mediano de la vivienda (MedHouseVal)')

st.pyplot(fig2)

fig3, ax = plt.subplots()




