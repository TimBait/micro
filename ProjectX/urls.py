from django.urls import path, include
from users import views
from drf_yasg.views import get_schema_view  # new
from drf_yasg import openapi  # new
from rest_framework import permissions
from django.views.generic import TemplateView

schema_view = get_schema_view(  # new
    openapi.Info(
        title="Test API",
        default_version='v1',
        description="Test description",
    ),
    # url=f'{settings.APP_URL}/api/v3/',
    patterns=[path('', include('users.urls')), ],
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path(
        'swagger-ui/',
        TemplateView.as_view(
            template_name='swaggerui/swaggerui.html',
            extra_context={'schema_url': 'openapi-schema'}
        ),
        name='swagger-ui'),
    path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'),
]
urlpatterns = [
    path('api/', include('users.urls'))
    #path('autorization/', views.autorization),
    #path('profile_settings/', views.profile_settings),
    #path('login/', views.micro_auth),
    #path('user/', views.User.as_view({'get': 'list'}), name='user'),
    #path('', include('users.urls')),
]