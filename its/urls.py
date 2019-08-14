"""its URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from itsapp import views as user_views

import itsapp.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^$', itsapp.views.index, name='firstpage'),
    url(r'^join/$', itsapp.views.join, name='join'),
    url(r'^login/', auth_views.login, {'template_name': 'itsapp/login.html'}, name='login'),
    url(r'^logout/', auth_views.logout, {'template_name' : 'itsapp/logged_out.html'}, name='logout'),
    url(r'^profile/', itsapp.views.profile, name='profile'),
    url(r'^home/$', itsapp.views.home, name='home'),
    url(r'^board/', include('board.urls', namespace='board')),
    url(r'ckeditor/', include('ckeditor_uploader.urls')),
    url(r'hitcount/', include('hitcount.urls', namespace='hitcount')),
    url(r'post/', include('post.urls', namespace='post')),
    url(r'oauth/', include('social_django.urls', namespace='social')),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

