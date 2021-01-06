from . views import StatusViewset, StatusAPIView
from django.urls import include, path

urlpatterns = [
    path('crud/', StatusViewset.as_view()),
    path('mixins/', StatusAPIView.as_view())

]
