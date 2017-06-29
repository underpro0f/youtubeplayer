from django.conf.urls import include, url
from . import views

from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required

urlpatterns = [
    #url(r'^$',  never_cache(views.about), name='about'),
    url(r'^new/$', views.new_room, name='new_room'),
    url(r'^list_rooms/$', views.chat_list_rooms, name='chat_list_rooms'),
    #url(r'^private/(?P<title>[\w-]{,50})/$', never_cache(login_required(views.PrivateGroupView.as_view())), name='new_privateroom_edit'),
    url(r'^list_rooms/(?P<title>[\w-]{,50})/$', views.chat_room, name='groupchat_index'),
    url(r'^$', views.index, name='chat_index'),
    #url(r'^private/$', views.new_room_private, name='new_room_private'),
    url(r'^private/$', never_cache(login_required(views.PrivateGroupEditView.as_view())), name="new_room_private"),
    #url(r'^private/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_members, name="change_members"),
    #url(r'^private/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_friends, name="change_friends"),

]
