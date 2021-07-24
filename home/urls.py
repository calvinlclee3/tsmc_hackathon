from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

urlpatterns = [
    path('', login_required(
        TemplateView.as_view(template_name='home/index.html')), name='home'),
]
