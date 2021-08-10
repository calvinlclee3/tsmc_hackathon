from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.conf.urls import url
from . import views

urlpatterns = [


    path('', login_required(
        TemplateView.as_view(template_name='home/index.html')), name='home'),
    url(
        regex=r'^register/$',
        view=views.RegisterView.as_view(),
        name='register'
    ),

    url(
        regex=r'^login/$',
        view=views.LoginView.as_view(),
        name='login'
    ),
    url(
        regex=r'^logout/$',
        view=views.LogoutView.as_view(),
        name='logout'
    ),

    url(
        regex=r'^members/$',
        view=views.MembersView.as_view(),
        name='members'
    ),        
    
    url(
        regex=r'^file/$',
        view=views.FileView.as_view(),
        name='file'
    ),

    url(
        regex=r'^info/$',
        view=views.MembersView.as_view(),
        name='info'
    ),
    url(
        regex=r'^fullcalendar/',
        view=TemplateView.as_view(template_name="fullcalendar/fullcalendar.html"),
        name='fullcalendar'
    )
    
    
]
