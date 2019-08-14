from django.conf.urls import url
import board.views
from board.views import *


urlpatterns = [
    url(r'^$', BoardListView.as_view(), name='index'),
    url(r'^add/$', BoardCreateView.as_view(), name='add'),
    url(r'^(?P<pk>[0-9]+)/$', BoardDetailView.as_view(), name='view'),
    url(r'^(?P<pk>[0-9]+)/edit/$', BoardUpdateView.as_view(), name='edit'),
    url(r'^(?P<pk>[0-9]+)/delete/$', BoardDeleteView.as_view(), name='delete'),
]
