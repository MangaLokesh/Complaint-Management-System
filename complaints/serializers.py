from rest_framework import serializers
from .models import Complaint

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = ["id","title","description","room_no","status", "created_at"]
        read_only_fields = ["user", "status", "created_at"]
