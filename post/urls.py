from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from post.views import *

urlpatterns = [
    url(r'^new/$', PostCreateView.as_view(), name='new'),
    url(r'^$', PostListView.as_view(), name='list'),
    url(r'^tag/(?P<tag>[^/]+(?u))/$', PostTOL.as_view(), name="tagged_object_list"),
    url(r'^c_lang/', C_ListView.as_view(), name='c_list'),
    url(r'^c_plus_lang/', C_Plus_ListView.as_view(), name='c_plus_list'),
    url(r'^python_lang/', Python_ListView.as_view(), name='python_list'),
    url(r'^java_lang/', Java_ListView.as_view(), name='java_list'),
    url(r'^hp_elec/', HP_ListView.as_view(), name='hp_list'),
    url(r'^nb_elec/', NB_ListView.as_view(), name='nb_list'),
    url(r'^kb_elec/', KB_ListView.as_view(), name='kb_list'),
    url(r'^ep_elec/', EP_ListView.as_view(), name='ep_list'),
    url(r'^notice/$', AddNotice, name='add_notice'),
    url(r'^(?P<pk>[0-9]+)/delete/$', PostDeleteView.as_view(), name='post_delete'),
    url(r'^mypost/$', My_ListView.as_view(), name='mypost'),
    url(r'^(?P<username>\w+)/list/$', Other_ListView.as_view(), name='other_list'),
    url(r'^(?P<pk>[0-9]+)/comment/$', CommentDetailView.as_view(), name='comment'),
    url(r'^(?P<pk>[0-9]+)/comment/new/$', CommentCreateView.as_view(), name='comment_new'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)