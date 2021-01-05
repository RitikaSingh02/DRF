from . views import StatusViewset
from django.urls import include, path

urlpatterns = [
    path('crud/', StatusViewset.as_view())
]
