from django.urls import path

from . import views

app_name = 'drf_error_handling'

urlpatterns = [
    path('', views.ExceptionView.as_view(), name='index'),
]
