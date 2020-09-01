from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.ThemeListView.as_view(), name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^change_profile/$', views.change_profile, name='change_profile'),
    url(r'^theme/(?P<pk>\d+)$', views.ThemeDetailView.as_view(), name='theme-detail'),
    url(r'^post/(?P<pk>\d+)$', views.post, name='post-detail'),
    url(r'^post/add/$', login_required(views.PostCreate.as_view()), name='post_create'),
    url(r'^theme/add/$', login_required(views.ThemeCreate.as_view()), name='theme_create'),
    url(r'^post/(?P<pk>\d+)/delete/$', login_required(views.PostDelete.as_view()), name='post_delete'),
    url(r'^theme/(?P<pk>\d+)/delete/$', login_required(views.ThemeDelete.as_view()), name='theme_delete'),
    url(r'^comm/(?P<pk>\d+)/delete/$', login_required(views.CommentDelete.as_view()), name='comm_delete'),
]
