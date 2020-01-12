from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('app1', include('test_app.urls')),
    path('', views.IndexView.as_view()),
]
