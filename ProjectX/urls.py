from django.urls import path
from users import views
from django.conf.urls import include
from rest_framework import routers, serializers, viewsets
from users.serializers import UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
#router = routers.DefaultRouter()
#router.register(r'users', User, basename='users')


urlpatterns = [
    path('autorization/', views.autorization),
    path('profile_settings/', views.profile_settings),
    path('login/', views.micro_auth),
    #path('user/', views.User.as_view({'get': 'list'}), name='user'),
    path('', include('users.urls')),
]