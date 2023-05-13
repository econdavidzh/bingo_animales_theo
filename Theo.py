import glob
import os
import random
import streamlit as st

def obtener_archivos_en_carpeta(ruta_carpeta):
    archivos = glob.glob(os.path.join(ruta_carpeta, '*'))
    return archivos

# Ruta de la carpeta que deseas explorar
ruta_carpeta = "Animales"

def main():
    st.title("Bingo Theo!")
    
    try:
        lista_animales = lista_animales
    except:
        lista_animales = obtener_archivos_en_carpeta(ruta_carpeta)
    
    # Botón para mostrar una imagen aleatoria
    if st.button("Selección aleatoria de un animalito :D"):
        
        # Obtener una imagen aleatoria
        imagen_aleatoria = random.choice(lista_animales)
        lista_animales = lista_animales.remove(imagen_aleatoria)
        
        if imagen_aleatoria:
            # Mostrar la imagen
            try:
                titulo = imagen_aleatoria.split('_')[1].split('.')[0]
                st.image(imagen_aleatoria)
                st.title('Letra: ' + imagen_aleatoria.split('_')[0].split('/')[1])
                st.title(titulo)
            
            except:
                st.write("Se acabaron los animalitos del bingo :(")
                
        else:
            st.write("No se encontraron imágenes en el directorio.")
    

if __name__ == "__main__":
    main()
