from rest_framework import viewsets
from .serializer import WasteSerializer
from .models import Waste
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class WasteView(viewsets.ModelViewSet):
  serializer_class = WasteSerializer
  queryset = Waste.objects.all()
  parser_classes = [MultiPartParser, FormParser]

  def create(self, request, format=None):
        print("llega",request.data)
        serializer = WasteSerializer(data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_200_OK)
        else:
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)