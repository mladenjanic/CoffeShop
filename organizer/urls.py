from django.conf.urls import include, url
from .views import TagList, TagPageList, tag_detail, StartupList, startup_detail, TagCreate, StartupCreate, NewsLinkCreate, NewsLinkUpdate, TagUpdate, StartupUpdate, NewsLinkDelete, TagDelete, StartupDelete

urlpatterns = [
    url(r'^tag/$', TagList.as_view(), name='organizer_tag_list'),
    url(r'^tag/(?P<page_number>\d+)/$', TagPageList.as_view(), name='organizer_tag_page'),
    url(r'^tag/create/$', TagCreate.as_view(), name='organizer_tag_create'),
    url(r'^tag/(?P<slug>[\w\-]+)/$', tag_detail, name='organizer_tag_detail'),
    url(r'^tag/(?P<slug>[\w\-]+)/update/$', TagUpdate.as_view(),                               name='organizer_tag_update'),
    url(r'^tag/(?P<slug>[\w\-]+)/delete/$', TagDelete.as_view(),                               name='organizer_tag_delete'),
    url(r'^startup/$', StartupList.as_view(), name='organizer_startup_list'),
    url(r'^startup/create/$', StartupCreate.as_view(), name='organizer_startup_create'),
    url(r'^startup/(?P<slug>[\w\-]+)/$', startup_detail, 
        name='organizer_startup_detail'),
    url(r'^startup/(?P<slug>[\w\-]+)/update/$', StartupUpdate.as_view(),                       name='organizer_startup_update'),
    url(r'^startup/(?P<slug>[\w\-]+)/delete/$', StartupDelete.as_view(),                       name='organizer_startup_delete'),
    url(r'^newslink/create/$', NewsLinkCreate.as_view(), name='organizer_newslink_create'),
    url(r'^newslink/update/(?P<pk>\d+)/$', NewsLinkUpdate.as_view(),                           name='organizer_newslink_update'),
    url(r'^newslink/delete/(?P<pk>\d+)/$', NewsLinkDelete.as_view(),                           name='organizer_newslink_delete'),
    
]