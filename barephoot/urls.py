from django.conf.urls import patterns,url
from barephoot import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.views import APIView
from django.conf.urls import include

urlpatterns = patterns('',
url(r'^$',views.index,name='index'),
url(r'^about/',views.about,name='about'),

url(r'^list/mov',views.MovList.as_view(),name='list'),
url(r'^detail/mov(?P<id>[0-9])+/',views.MovDetail.as_view(),name='detail'),

url(r'^list/res',views.ResList.as_view(),name='list'),
url(r'^detail/res(?P<id>[0-9])+/',views.ResDetail.as_view(),name='detail'),

url(r'^list/places',views.PlacesList.as_view(),name='list'),
url(r'^detail/places(?P<id>[0-9])+/',views.PlacesDetail.as_view(),name='detail'),

url(r'^list/events',views.EventList.as_view(),name='list'),
url(r'^detail/events(?P<id>[0-9])+/',views.EventsDetail.as_view(),name='detail'),

url(r'^users/$', views.UserList.as_view()),
url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += [url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),]