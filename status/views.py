from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from status.serializers.serializers import StatusSerializer
from .models import Status
from rest_framework import mixins, generics, permissions
from rest_framework.authentication import SessionAuthentication


class StatusViewset(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)

        return JsonResponse(serializer.data, safe=False)


class StatusAPIView(generics.ListAPIView, mixins.CreateModelMixin):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [SessionAuthentication]
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    # if i change the func name from get to something else then the drf admin panel will show else normal web page is displayed
    def getusers(self, request, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        print(request.user)
        return self.create(request, *args, **kwargs)


# Create your views here.
