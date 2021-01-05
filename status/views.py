from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from status.serializers.serializers import StatusSerializer
from .models import Status


class StatusViewset(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)

        return JsonResponse(serializer.data, safe=False)


# Create your views here.
