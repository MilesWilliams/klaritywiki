from django.conf.urls import url
from django.core.urlresolvers import reverse
from . import views

app_name = 'wiki'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),
    url(r'^categories/(?P<pk>[0-9]+)/edit/$', views.AlbumUpdate.as_view(), name='edit_category'),
    # url(r'^(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]
