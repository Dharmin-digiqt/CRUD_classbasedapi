from .models import Students
from rest_framework import serializers


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        # fields = '__all__'
        fields = ["id", "e_no", "name", "city", "branch"]
