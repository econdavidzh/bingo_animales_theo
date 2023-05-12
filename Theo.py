import glob
import os
import random

def obtener_archivos_en_carpeta(ruta_carpeta):
    archivos = glob.glob(os.path.join(ruta_carpeta, '*'))
    return archivos

# Ruta de la carpeta que deseas explorar
ruta_carpeta = "Animales"


import streamlit as st


def main():
    st.title("Bingo Theo!")
    
    # Botón para mostrar una imagen aleatoria
    if st.button("Selección aleatoria de un animalito :D"):
        # Obtener una imagen aleatoria
        lista_animales = obtener_archivos_en_carpeta(ruta_carpeta)
        imagen_aleatoria = random.choice(lista_animales)
        
        if imagen_aleatoria:
            # Mostrar la imagen
            titulo = imagen_aleatoria.split('_')[1].split('.')[0]
            st.image(imagen_aleatoria, caption=titulo)
        else:
            st.write("No se encontraron imágenes en el directorio.")
    

if __name__ == "__main__":
    main()
