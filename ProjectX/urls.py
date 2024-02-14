from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from users import views
from django.urls import path, include
from django.views.generic import RedirectView



urlpatterns = [
    #path('autorization/', views.autorization),
    #path('profile_settings/', views.profile_settings),
    #path('login/', views.micro_auth),
    path('', RedirectView.as_view(url='api/schema/swagger-ui/')), # Перенаправление на Swagger UI
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('users/', include('users.urls')),  # Подключение путей из приложения users
]
