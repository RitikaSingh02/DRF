from . views import StatusViewset, StatusAPIView, AuthView
from django.urls import include, path

urlpatterns = [
    path('crud/', StatusViewset.as_view()),
    path('mixins/', StatusAPIView.as_view()),
    path('jwt/', AuthView.as_view()),
    # path('check/', check)
]
