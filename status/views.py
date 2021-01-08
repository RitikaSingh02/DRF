from rest_framework_jwt.views import verify_jwt_token
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from status.serializers.serializers import StatusSerializer
from .models import Status
from rest_framework import mixins, generics, permissions
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from status.JWT_MODIFICATIONS.jwt_custom_payload import jwt_response_payload_handler
from rest_framework_jwt.utils import jwt_payload_handler
from rest_framework_jwt.utils import jwt_encode_handler
import json
import requests


class StatusViewset(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)

        return JsonResponse(serializer.data, safe=False)

# we do not need to store the jwt tokens https://stackoverflow.com/questions/47407536/how-to-store-jwt-token-in-db-with-django-rest-framework


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

# class AuthView(APIView):
#     permission_classes = [permissions.AllowAny]
#     authentication_classes = [TokenAuthentication]

#     def post(self, request, *args, **kwargs):
#         # print(request.user)
#         if request.user.is_authenticated:
#             return JsonResponse({'msg': "you are already authenticated"}, status=200)
#         data = json.loads(request.body)
#         username = data['username']
#         password = data['password']
#         email = data['email']
#         qs = User.objects.filter(username__iexact=username)
#         if qs.exists():
#             user = authenticate(username=username, password=password)
#             # print(user)
#             if user is not None:
#                 if user.is_active:
#                     user_obj = User.objects.get(
#                         username__iexact=username)
#                     # print(user_obj)
#                     payload = jwt_payload_handler(user_obj)
#                     token = jwt_encode_handler(payload)
#                     response = jwt_response_payload_handler(
#                         token, user_obj, request=request)
#                     # print(response)
#                     return JsonResponse(response, safe=False)  # token returned
#                 return JsonResponse({'msg': "invalid credentials"}, safe=False)
#             return JsonResponse({'msg': "not authorised to access this"}, safe=False)
#             # return JsonResponse({'msg': "user already exists"}, safe=False)
#         else:
#             user = User.objects.create(username=username, email=email)
#             user.set_password(password)
#             user.save()
#             # payload = jwt_payload_handler(user)
#             # token = jwt_encode_handler(payload)
#             # response = jwt_response_payload_handler(
#             #     token, user, request=request)
#             # print(response)
#             return JsonResponse({'msg': "user created proceed to login"}, safe=False)


class AuthView(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = [TokenAuthentication]

    def post(self, request, *args, **kwargs):
        # print(request.user)
        if request.user.is_authenticated:
            return JsonResponse({'msg': "you are already authenticated"}, status=200)
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        email = data['email']
        # user_token = data['jwt']
        qs = User.objects.filter(username__iexact=username)
        if qs.exists():
            user = authenticate(username=username, password=password)
            # print(user)
            if user is not None:
                if user.is_active:
                    user_obj = User.objects.get(
                        username__iexact=username)
                    # print(user_obj)
                    payload = jwt_payload_handler(user_obj)
                    token = jwt_encode_handler(payload)
                    response_payload = jwt_response_payload_handler(
                        token, user_obj, request=request)
                    print(response_payload)
                    response = requests.post("http://127.0.0.1:8080/api/jwt-verify/",
                                             {"token": token})
                    print(response)
                    return JsonResponse({'msg': "token is verified", 'token': response_payload['token']}, safe=False, status=response.status_code)
                    # use the above token set in response to verify on the url /api/jwt-verify/ else the below error is shown
                    # The `request` argument must be an instance of `django.http.HttpRequest`, not `builtins.dict`
                return JsonResponse({'msg': "invalid credentials"}, safe=False)
            return JsonResponse({'msg': "not authorised to access this"}, safe=False)
            # return JsonResponse({'msg': "user already exists"}, safe=False)
        else:
            user = User.objects.create(username=username, email=email)
            user.set_password(password)
            user.save()
            return JsonResponse({'msg': "user created proceed to login"}, safe=False)


##do not try the below method##
# def check(request):

#     token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjEwMTA1OTM0LCJlbWFpbCI6InJpdGlrYUBnbWFpbC5jb20ifQ.8hnUebdwPqX0PYSoFJqnIKUF9Q4T8_gaEFpoxEELeu8"

#     def verify(token):
#         verify_jwt_token({'token': token})

#     print(verify(token))
#     return JsonResponse('prt', safe=False)
# Create your views here.
