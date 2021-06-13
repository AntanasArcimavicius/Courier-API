from rest_framework import serializers

from .models import Courier


class CourierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Courier
        fields = ('name', 'start_time', 'end_time',)
        extra_kwargs = {
            'start_time': {'format': '%H:%M'},
            'end_time': {'format': '%H:%M'},
            }


class FileUploadSerializer(serializers.Serializer):
    courier_list = serializers.FileField()

    class Meta:
        fields = ('courier_list',)