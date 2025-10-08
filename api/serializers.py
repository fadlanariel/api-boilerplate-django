from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "name", "description", "owner", "created_at"]
        read_only_fields = ["owner", "created_at"]
