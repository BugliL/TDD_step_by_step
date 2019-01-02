from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello world')


def function_index():
    pass
