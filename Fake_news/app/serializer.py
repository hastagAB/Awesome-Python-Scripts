from rest_framework import serializers
from .models import FakeNews_model


class FakeNews_Serializer(serializers.ModelSerializer):
    class Meta:
        model = FakeNews_model
        fields =['title', 'text', 'subject','date']
        