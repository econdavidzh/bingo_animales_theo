import glob
import os
import random
import streamlit as st

animales_seleccionados = []
count = 0
animals_dict = dict()

def obtener_archivos_en_carpeta(ruta_carpeta):
    archivos = glob.glob(os.path.join(ruta_carpeta, '*'))
    return archivos

def obtener_elemento_aleatorio(lista):
    if len(lista) == 0:
        return None
    # Seleccionar un elemento aleatorio de la lista
    elemento_seleccionado = random.choice(lista)
    # Eliminar el elemento seleccionado de la lista
    lista.remove(elemento_seleccionado)
    return elemento_seleccionado

# Ruta de la carpeta que deseas explorar
lista_animales = obtener_archivos_en_carpeta("Animales")

st.title("Bingo Theo!")
        
# Botón para mostrar una imagen aleatoria
if st.button("Selección aleatoria de un animalito :D"):
    count += 1
    lista_animales = [for x in lista_animales if x not in animales_seleccionados]
    # Obtener una imagen aleatoria
    imagen_aleatoria = obtener_elemento_aleatorio(lista_animales)
    animals_dict[count] = imagen_aleatoria
    
    if imagen_aleatoria:
        # Mostrar la imagen
        imagen_aleatoria = obtener_elemento_aleatorio(lista_animales)
        animales_seleccionados += [imagen_aleatoria]
        try:
            titulo = imagen_aleatoria.split('_')[1].split('.')[0]
            st.image(imagen_aleatoria)
            st.title('Letra: ' + imagen_aleatoria.split('_')[0].split('/')[1] + ' - Animal: ' + titulo)
            st.write(animals_dict)
            
        except:
            st.write("Se acabaron los animalitos del bingo :(")
