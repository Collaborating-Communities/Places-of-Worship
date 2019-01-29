from django.conf.urls import url
from .views import CommunityListsApi, CommunityArticlesApi

urlpatterns = [
	url(r'^list/$', CommunityListsApi.as_view(), name='community-list-api'),
    url(r'^articles/(?P<pk>\d*)/$', CommunityArticlesApi.as_view(), name='community-articles-api'),
	]
