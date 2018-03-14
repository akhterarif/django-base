from django_filters.rest_framework import CharFilter
from base.api.filtersets import BaseFilterSet
from ...models import PostModel

class PostFilterSet(BaseFilterSet):
	title = CharFilter(name="title", lookup_expr='icontains')
	text = CharFilter(name="text", lookup_expr='icontains')
	category__name = CharFilter(name="category__name", lookup_expr='icontains')

	class Meta:
		model = PostModel
		fields = ['category__name', 'title', 'text']