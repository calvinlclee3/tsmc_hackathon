from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(
        TemplateView.as_view(template_name='core/chat.html')), name='chat'),
]
