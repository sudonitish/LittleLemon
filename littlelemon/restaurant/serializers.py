from rest_framework import serializers
from .models import MenuTable
from .models import Booking


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuTable
        fields = "__all__"

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
