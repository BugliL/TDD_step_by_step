from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.IndexView.as_view()),
    path('LiveServerTestCase',
         TemplateView.as_view(template_name='LiveServerTestCase.html'),
         name='LiveServerTestCase'),
]
