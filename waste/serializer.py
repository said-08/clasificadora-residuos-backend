from rest_framework import serializers
from .models import Waste

class WasteSerializer(serializers.ModelSerializer):
  label = serializers.CharField(required=False)
  class Meta:
    model = Waste
    fields = ('id', 'img', 'description', 'label')
    
  def get_label(self, obj):
      if not obj.label:
          # Si el campo 'label' no está presente o es vacío, asignar el valor clasificado
          image_path = obj.img.path
          label = self.context['view'].classify_image(image_path)
          return label
      return obj.label