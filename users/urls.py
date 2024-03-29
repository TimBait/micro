from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from users import views


router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='users')


urlpatterns = [
    path('', include(router.urls)),
    # API Schema:
    #path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    #path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
