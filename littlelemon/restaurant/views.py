from django.shortcuts import render
from rest_framework import generics
from .models import MenuTable, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

def index(request):
    return render(request, "index.html", {})


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuTable.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]



class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuTable.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
