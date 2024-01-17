from django.http import HttpResponse
from django.template import loader


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
