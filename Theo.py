import glob
import os
import random
import streamlit as st

def obtener_archivos_en_carpeta(ruta_carpeta):
    archivos = glob.glob(os.path.join(ruta_carpeta, '*'))
    return archivos

# Ruta de la carpeta que deseas explorar
lista_animales = obtener_archivos_en_carpeta("Animales")

st.title("Bingo Theo!")
        
# Botón para mostrar una imagen aleatoria
if st.button("Selección aleatoria de un animalito :D"):
    # Obtener una imagen aleatoria
    imagen_aleatoria = obtener_elemento_aleatorio(lista_animales)
    if imagen_aleatoria:
        # Mostrar la imagen
        imagen_aleatoria = random.choice(lista_animales)
        titulo = imagen_aleatoria.split('_')[1].split('.')[0]
        st.image(imagen_aleatoria)
        st.title('Letra: ' + imagen_aleatoria.split('_')[0].split('/')[1] + ' - Animal: ' + titulo)
