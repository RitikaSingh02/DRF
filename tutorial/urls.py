from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
#https://www.django-rest-framework.org/api-guide/routers/
from quickstart import views
from quickstart.views import ArticleViewSet
from quickstart import urls

# REST framework adds support for automatic URL routing to Django(similar to rails),
# and provides you with a simple, 
# quick and consistent way of wiring your view logic to a set of URLs.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)#register(prefix,viewsets,basename)#basename is optinal
# The basename argument is used to specify the initial part of the view name pattern. In the example above,
# that's the users or groups part.
router.register(r'groups', views.GroupViewSet)
router.register(r'articles',views.ArticleViewSet,basename="articles")#basename attribute is compulsory if the viewsetdoes not have a queryset attribute
##error like 
    #::AssertionError: `basename` argument not specified, and could not automatically determine the name from the viewset, as it does not have a `.queryset` attribute
    #is generated
router.register(r'new-api',views.UserNewViewSet,basename="new")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
 #this creates us three form of url pattern from our urls
    # http://localhost:8000/
    #     ^$ [name='api-root']
    #     ^users/$ [name='user-list']
    #     ^users\.(?P<format>[a-z0-9]+)/?$ [name='user-list']
    #     ^users/(?P<pk>[^/.]+)/$ [name='user-detail']
    #     ^users/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='user-detail']
    #     ^groups/$ [name='group-list']
    #     ^groups\.(?P<format>[a-z0-9]+)/?$ [name='group-list']
    #     ^groups/(?P<pk>[^/.]+)/$ [name='group-detail']
    #     ^groups/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='group-detail']
    #     ^new/$ [name='user-list']
    #     ^new\.(?P<format>[a-z0-9]+)/?$ [name='user-list']
    #     ^new/(?P<pk>[^/.]+)/$ [name='user-detail']
    #     ^new/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='user-detail']
    
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/',admin.site.urls),
    path('app/',include('quickstart.urls')),
]
