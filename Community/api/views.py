from Community.models import Community, CommunityArticles
from .serializers import CommunitySerializer, CommunityArticlesSerializer, CommunityMediaSerializer
from rest_framework import generics

class CommunityListsApi(generics.ListAPIView):
	queryset = Community.objects.all()
	serializer_class = CommunitySerializer


class CommunityArticlesApi(generics.ListAPIView):
	serializer_class = CommunityArticlesSerializer
	lookup_url_kwarg = 'pk'

	def get_queryset(self):
		return CommunityArticles.objects.filter(article__state__name='publish', community = self.kwargs['pk'])