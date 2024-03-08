import cv2
import tensorflow as tf
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf

model = tf.keras.models.load_model('C:/Users/leonel.martinez/Desktop/ModeloEntrenado/modelo_entrenado.h5')

img_height = 224
img_width = 224

def preprocess_image(image):
    # Redimensionar la imagen
    image = cv2.resize(image, (img_height, img_width))
    # Normalizar los valores de píxel
    image = image / 255.0
    # Agregar una dimensión para que coincida con la forma de entrada del modelo
    image = np.expand_dims(image, axis=0)
    return image

def classify_image(image_path):
    # Leer la imagen
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: No se pudo leer la imagen {image_path}")
        return
    
    # Preprocesar la imagen
    preprocessed_image = preprocess_image(image)

    # Clasificar la imagen utilizando el modelo
    predictions = model.predict(preprocessed_image)

    # Obtener la clase con la probabilidad más alta
    predicted_class = np.argmax(predictions)
    label = ""
    # Mostrar el resultado
    if predicted_class == 0:
        label = "blanco"
        print("La imagen es un residuo blanco. " + label)
        print("Recuerda que debes lavarlos y dejarlos secar antes de tirarlos")
        
        return label
    elif predicted_class == 1:
        label = "negro"
        print("La imagen es un residuo negro. " + label)        
        return label
    elif predicted_class == 2:
        label = "verde"
        print("La imagen es un residuo verde. " + label)         
        return label
    else:
        print("La imagen es irreconocible.")

# Ejemplo de uso
print("Escriba salir para terminar")

# desde acá se puede modificar para la lógica de lectura
# de la imagen
while True:
    #  Acá serializer Daniel Wendy
    # serializer.data.img
    image_path = input("Ingrese la ruta de la imagen (o escriba 's' para terminar): ")
    if image_path.lower() == 's':
        print("saliendo... hasta pronto!")
        break
    classify_image(image_path)