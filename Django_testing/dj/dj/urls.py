from django.urls import path, include

from . import views

urlpatterns = [
    path('app1', include('test_app.urls')),
    path('error_test', include('drf_error_handling.urls')),
    path('', views.IndexView.as_view()),
]
