from django.shortcuts import render
from rest_framework import generics
from .models import MenuTable, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

def index(request):
    return render(request, "index.html", {})

@permission_classes([IsAuthenticated])
class MenuItemsView(generics.ListCreateAPIView):
   permission_classes = [IsAuthenticated]
   queryset = MenuTable.objects.all()
   serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuTable.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
