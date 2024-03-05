from rest_framework import viewsets
from .serializer import WasteSerializer
from .models import Waste

# Create your views here.
class WasteView(viewsets.ModelViewSet):
  serializer_class = WasteSerializer
  queryset = Waste.objects.all()