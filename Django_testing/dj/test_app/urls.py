from django.urls import path, include
from django.views.generic import TemplateView

from . import views

app_name = 'app1'

urlpatterns = [

    path('', views.function_index, name='index'),

    path('LiveServerTestCase/',
         TemplateView.as_view(template_name='LiveServerTestCase.html'),
         name='LiveServerTestCase'),
]
