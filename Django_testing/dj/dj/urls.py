from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'dj'

urlpatterns = [

    path('', views.IndexView.as_view()),
    path('index', views.function_index, name='index'),

    path('LiveServerTestCase',
         TemplateView.as_view(template_name='LiveServerTestCase.html'),
         name='LiveServerTestCase'),
]
