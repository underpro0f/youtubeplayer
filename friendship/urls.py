from django.conf.urls import include, url
from . import views
#from .views import FriendView

from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', never_cache(login_required(views.FriendView.as_view())), name='friend_index'),
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_friends, name="change_friends"),

]
