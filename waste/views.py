from rest_framework import viewsets
from .serializer import WasteSerializer
from .models import Waste
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import cv2
import tensorflow as tf
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from pathlib import Path
# Create your views here.  
from rest_framework import viewsets, status
import djangoClasificadorBackend

class WasteView(viewsets.ModelViewSet):
    serializer_class = WasteSerializer
    queryset = Waste.objects.all()
    parser_classes = [MultiPartParser, FormParser]

    def preprocess_image(self, image):
        # Redimensionar la imagen
        img_height = 224
        img_width = 224
        image = cv2.resize(image, (img_height, img_width))
        # Normalizar los valores de píxel
        image = image / 255.0
        # Agregar una dimensión para que coincida con la forma de entrada del modelo
        image = np.expand_dims(image, axis=0)
        return image

    def classify_image(self, image_path):
        # Leer la imagen
        ruta_completa = image_path.replace('\\','\\\\') #C:\\Users\\leonel.martinez\\Desktop\\SaidMain\\SaidMain\\clasificadora-residuos-backend\\media\\posts" + image_path
        print ("martinez" + image_path + "Leoces")
        print("RUTA COMPLETA", ruta_completa, "hasta aqui")
        image = cv2.imread(ruta_completa)
        #print("prueba Imagen", image)
        if image is None:
            print(f"Error: No se pudo leer la imagen {image_path}")
            label = "prueba"
            return None

        # Preprocesar la imagen
        preprocessed_image = self.preprocess_image(image)

        # Cargar el modelo de TensorFlow
        model_path = 'C:\\Users\\said.salcedo\\Documents\\DEV\\modelo_entrenado.h5'
       # 
        model = tf.keras.models.load_model(model_path)

        # Clasificar la imagen utilizando el modelo
        predictions = model.predict(preprocessed_image)

        # Obtener la clase con la probabilidad más alta
        predicted_class = np.argmax(predictions)
        label = ""
        # Mostrar el resultado
        if predicted_class == 0:
            label = "blanco"                 
        elif predicted_class == 1:
            label = "negro"                
        elif predicted_class == 2:
            label = "verde"
        else:
            print("La imagen es irreconocible.")
        return label

    def create(self, request, format=None):
    # Serializar los datos recibidos en la solicitud POST
      serializer = WasteSerializer(data=request.data)
      if serializer.is_valid():
        # Si los datos son válidos, guardar el objeto Waste en la base de datos
        serializer.save()

        # Obtener la ruta de la imagen asociada al objeto Waste y clasificarla
        image_path = serializer.instance.img.path
        label = self.classify_image(image_path)

        # Actualizar el campo 'label' en el objeto Waste con la etiqueta clasificada
        serializer.instance.label = label
        serializer.instance.save()

        # Devolver la respuesta con el objeto serializado y el código de estado HTTP 201 CREATED
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      else:
        # Si los datos no son válidos, devolver una respuesta con los errores de validación y el código de estado HTTP 400 BAD REQUEST
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)