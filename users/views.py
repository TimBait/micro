from django.template import loader
from django.http import HttpResponse
from users.models import User
from users.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    #@action(detail=True)
    #def highlight(self, request, *args, **kwargs):
        #user = self.get_object()
        #return Response(user.highlighted)   #метод изменения определенных данных

    #def perform_create(self, serializer):
        #serializer.save()



def micro_auth(request):
    template = loader.get_template('login.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)


def autorization(request):
    template = loader.get_template('autorization.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)


def profile_settings(request):
    template = loader.get_template('profile_settings.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)
