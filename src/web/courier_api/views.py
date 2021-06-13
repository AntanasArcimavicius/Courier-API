from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import CourierSerializer, FileUploadSerializer
from .models import Courier
from .utils import check_if_time_is_valid, active_couriers_json

class CourierView(viewsets.ModelViewSet):

    serializer_class = CourierSerializer
    queryset = Courier.objects.all()

    def perform_create(self, serializer):
        check_if_time_is_valid(serializer)
        serializer.save()

    def perform_update(self, serializer):
        check_if_time_is_valid(serializer)
        serializer.save()


class FileUploadView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        active_couriers = active_couriers_json(serializer)

        return Response(active_couriers)
    

