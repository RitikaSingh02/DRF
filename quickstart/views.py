from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate,login,logout
from rest_framework import viewsets
from rest_framework import permissions
from quickstart.serializers import UserSerializer, GroupSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Article 
from django.views import View
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication
# from django.views.generic import View
from rest_framework.views import APIView
from .serializers import ArticleModelSerialiser
# from django.core.signals import user_logged_in
import json
import base64

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserNewViewSet(viewsets.ModelViewSet):
    #while using viewsets it is compulsory to define 
    # ::serializer_class(at any kind of hit)
    # ::queryset(MUST AT GET)(since authentication is being there from DRF)
    #(but in generic views it is not needed)
    # print("y")
    queryset=User.objects.all()
    serializer_class=UserSerializer
    # authentication_classes = (SessionAuthentication,)
    # permission_classes=[permissions.IsAuthenticated]
    # print(permission_classes)
    
    def create(self,request):#crestinga valid using user using POST
        data=json.loads(request.body)
        print(request.META)
        print(request.user)#AnonymousUser(it means the rest framework auth still do not recognises it)
        #print(request.body)#b'{\n    "username":"guddubhaiya.1923cs1078",\n    "email":"adam@gmail.com",\n    "password":"KIET123@s"\n\n}'
        if data["type_request"]=="create":
            #print(request)#<rest_framework.request.Request: POST '/new-api/'>
            serializer=UserSerializer(data=data)
            #print(serializer)
        #     UserSerializer(data={'username': 'ritika.1923cs1076', 'email': 'adam@gmail.com', 'password': 'adam'}):
        # username = CharField(help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, validators=[<django.contrib.auth.validators.UnicodeUsernameValidator object>, <UniqueValidator(queryset=User.objects.all())>])
        # email = EmailField(allow_blank=True, label='Email address', max_length=254, required=False)
        # password = CharField(max_length=128)
            if serializer.is_valid():
                user=serializer.save()
                user.set_password(data["password"])
                token = Token.objects.create(user=user)
                print(token.key)#fb7f6bd1d90940efb58152f08efd883b7cbd4826
                #HTTP_AUTHORIZATION': 'Token f147069a2f2a9dc55e492362d239db35cb8ae008'
                return JsonResponse({"user": UserSerializer(user, context=self.get_serializer_context()).data},safe=False)##(status code generated is 201)
            else:
                return JsonResponse(serializer.errors,safe=False)
        if data["type_request"]=="login":
            status=authenticate(username=data["username"],password=data["password"])
            print(status)
            user=User.objects.get(username=data["username"])
            print(user)#shivansh.1923cs1076
            if  user is not None:
                response=login(request,user)#null
                print(user.is_authenticated)#True
                print(request.session)#<django.contrib.sessions.backends.db.SessionStore object at 0x7f0c082f5e80>
                # print(request.META['HTTP_COOKIE'])#sessionid=ky8pp6z1p0m6znxtxq5efpllpe6wsnb0   (after successful login only this cookie is generated and for the same ssession that is until logout the sessionid remains the same )
                permission_classes=[permissions.IsAuthenticated]
                print(permission_classes)
                return JsonResponse(response,safe=False)
            else:
                return JsonResponse("nope",safe=False)  
        if data["type_request"]=="logout":
            status=authenticate(username=data["username"],password=data["password"])
            print(status)
            user=User.objects.get(username=data["username"])
            print(user)
            if  user is not None:
                response=logout(request)#null
                print(user.is_authenticated)#True
                print(request.session)#<django.contrib.sessions.backends.db.SessionStore object at 0x7f0c082f5e80>
                # print(request.META['HTTP_COOKIE'])#sessionid=ky8pp6z1p0m6znxtxq5efpllpe6wsnb0
                return JsonResponse(response,safe=False)
            else:
                return JsonResponse("nope",safe=False) 
            #here we need not to check EXISTS as DRF does this with the auth sys if a duplicate entry is given:(serializer.errors)
            # {
            #    "username": [
            #    "A user with that username already exists."
            #       ]
            # }##this error is raised(DRF DIFFERENTIATES BETWEEN USEERS WITH THEIR USERNAME ONLY!!!! WHICH IS THE ONLY RESONABLE THING )
            
###############################RESPONSE ATER SUCCESFULL CREATION############################3
                #{
                #   user": {
                #         "username": "shivansh.1923cs1076",
                #         "email": "adam@gmail.com",
                #         "password": "pbkdf2_sha256$150000$wwkRkUCLyTTW$c9PPC8sgnbKNeASrnmgokJf4jnAi+fieghH8OzFQHrQ="
                #          }
                # 
        if data["type_request"]=="session_authentication":
            authentication_classes = (SessionAuthentication,)
            # permission_classes = (IsAuthenticated,)
            status=authenticate(username=data["username"],password=data["password"])
            print(status)
            user=User.objects.get(username=data["username"])
            print(user)#shivansh.1923cs1076
            if  user is not None:
                response=login(request,user)#null
                print(user.is_authenticated)#True
                print(request.session)#<django.contrib.sessions.backends.db.SessionStore object at 0x7f0c082f5e80>
                # print(request.META['HTTP_COOKIE'])#sessionid=ky8pp6z1p0m6znxtxq5efpllpe6wsnb0   (after successful login only this cookie is generated and for the same ssession that is until logout the sessionid remains the same )
                permission_classes=[permissions.IsAuthenticated]
                print(permission_classes)
                return JsonResponse(response,safe=False)
            else:
                return JsonResponse("nope",safe=False)  
                
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Article.objects.filter(id=1).values()
    serializer_class = ArticleModelSerialiser
    
    #### THE ABOVE IS SAME TO:###

    # serializer_class=ArticleModelSerialiser
    # def get_queryset(self):#name of this func should not chage it is something DRF has inbuilt to understand that your viewset is returning a queryset
    #     return Article.objects.all()
    
#####RESPONSE####
#(by default a json type)
# HTTP 200 OK
# Allow: GET, POST, HEAD, OPTIONS
# Content-Type: application/json
# Vary: Accept

# [
#     {
#         "title": "this is the title",
#         "author": "taylor",
#         "email": "taylor@gmail.com",
#         "date": ""
#     },
#     {
#         "title": "this is title2",
#         "author": "adam",
#         "email": "adam@gmail.com",
#         "date": "22-11-2019"
#     }
# ]    

class ClassbasedViews(APIView):
    
    def get(self,request):
        # print(request.META)
        article=Article.objects.all()
        serializer=ArticleModelSerialiser(article,many=True)
        return JsonResponse(serializer.data,safe=False)

    def post(self,request):
        data=json.loads(request.body)
        # datas=JSONParser().parse(request)
        print(data)
        serializer=ArticleModelSerialiser(data=data)
        if serializer.is_valid():
            article=Article.objects.filter(email=serializer.data['email']).exists()
            if(article=="NULL"):
                Article(**serializer.data)
                return JsonResponse(serializer.data,safe=False)
            else:
                return JsonResponse("duplicate entry",safe=False,status=404)
        else:
            return JsonResponse(serializer.errors,safe=False,status=400)
# IF EMAIL FIELD IS WRONG
# {
#     "email": [
#         "Enter a valid email address."
#     ]
# }

#############DJANGO AUTHENTICATION###############

class Create_login_logout_View(View):
    def post(self,request):#crestinga valid using user using POST
        data=json.loads(request.body)
        print(request.META)
        print(request.user)#ritika.1923cs1076
        if data["type_request"]=="create":
            status=authenticate(username=data["username"],password=data["password"])
            print(status)
            if status==None:
                user, created = User.objects.get_or_create(username=data["username"])#if all gd created=True
                user.set_password(data['password'])
                user.save()
                return JsonResponse("user",safe=False)##(status code generated is 201)
            else:
                return JsonResponse("user not created",safe=False)
        if data["type_request"]=="login":
            status=authenticate(username=data["username"],password=data["password"])
            print(status)
            user=User.objects.get(username=data["username"])
            print(user)
            if  user is not None:
                response=login(request,user)#null
                print(user.is_authenticated)#True
                print(request.session)#<django.contrib.sessions.backends.db.SessionStore object at 0x7f0c082f5e80>
                # print(request.META['HTTP_COOKIE'])#sessionid=ky8pp6z1p0m6znxtxq5efpllpe6wsnb0   (after successful login only this cookie is generated and for the same ssession that is until logout the sessionid remains the same )
                return JsonResponse(response,safe=False)
            else:
                return JsonResponse("nope",safe=False)
        if data["type_request"]=="logout":
            status=authenticate(username=data["username"],password=data["password"])
            print(status)
            user=User.objects.get(username=data["username"])
            print(user)
            if  user is not None:
                response=logout(request)#null
                print(user.is_authenticated)#True
                print(request.session)#<django.contrib.sessions.backends.db.SessionStore object at 0x7f0c082f5e80>
                print(request.META['HTTP_COOKIE'])#sessionid=ky8pp6z1p0m6znxtxq5efpllpe6wsnb0
                return JsonResponse(response,safe=False)
            else:
                return JsonResponse("nope",safe=False)
            
#     {
#         "username": "perfect.entry",
#         "email": "adam@gmail.com",
#         "password": "KIET123",
#         "type_request":"login"
# }