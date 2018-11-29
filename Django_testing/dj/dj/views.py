from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('result')

