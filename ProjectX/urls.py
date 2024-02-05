from django.urls import path
from users import views
from django.conf.urls import include

urlpatterns = [
    path('autorization/', views.autorization),
    path('profile_settings/', views.profile_settings),
    path('login/', views.micro_auth),
    #path('user/', views.User.as_view({'get': 'list'}), name='user'),
    path('', include('users.urls')),
]