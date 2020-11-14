from django.urls import include, path
from .views import ClassbasedViews,Create_login_logout_View

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('article/',ClassbasedViews.as_view()),
    path('login/',Create_login_logout_View.as_view())
]