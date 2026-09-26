import streamlit as st
import pandas as pd

# Título de la app
st.title("Mi primer Dashboard con Streamlit")

# Texto explicativo
st.write("Esta es una app web creada completamente en Python.")

# Un slider interactivo
numero = st.slider("Selecciona un valor", 0, 100, 25)
st.write(f"El cuadrado del número es: **{numero ** 2}**")

# Mostrar una tabla de datos
datos = pd.DataFrame({
    'Categoría': ['A', 'B', 'C'],
    'Valores': [10, 20, 30]
})
st.dataframe(datos)