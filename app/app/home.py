from django.http import HttpResponse
from django.template import loader
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class Home(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        from django.utils.translation import gettext as _
        output = _("Hello World")
        return Response({"Message": output}, status=status.HTTP_200_OK)


def index(request):
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))
