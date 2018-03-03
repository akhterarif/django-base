from django_filters.rest_framework import CharFilter
from base.api.filtersets import BaseFilterSet
from ...models import PostModel

class PostFilterSet(BaseFilterSet):
	title = CharFilter(name="title", lookup_expr='icontains')
	text = CharFilter(name="text", lookup_expr='icontains')

	class Meta:
		model = PostModel
		fields = ['category', 'title', 'text']