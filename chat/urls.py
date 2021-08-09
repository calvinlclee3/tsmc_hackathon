from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from rest_framework.routers import DefaultRouter
from core.api import MessageModelViewSet, UserModelViewSet

router = DefaultRouter()
router.register(r'message', MessageModelViewSet, basename='message-api')
router.register(r'user', UserModelViewSet, basename='user-api')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path(r'api/v1/', include(router.urls)),
    path('chat/', include('core.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), {'next_page': '/'},
         name='logout')

]
